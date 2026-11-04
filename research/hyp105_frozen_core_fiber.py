"""AA4-FROZEN exact ORIGINAL W34 source cover palette restrictions.

Given a REAL original minimal source-ID cover T, the frozen source
columns F=I\\T do not change. Any legal zero-to-three GF5 ASET whose
edited support is contained in T must assign each i in T one of the
51 patterns that does NOT create a 2v2 or 3v3 source-disjoint equality
where every other ID is in F. A complete empty domain is a rigorous
NO-GO for THIS cover T. Nonempty domains do NOT prove feasibility.
"""
from collections import Counter
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import argparse
import json
import math

from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_original_gf5_deterministic_extraction_referee import PALETTES
from hyp105_w34_external_triple_r3_referee import exact_gf5_original_vectors
from hyp105_original_event_cover import normalize_edges,covers

ROOT=Path(__file__).parent
PARENT_721="25178580d7c820bdfc0c909c4f72df70ad38d2c2"
CERT_COVER=ROOT/"hyp105_w34_original_event_cover_certificates.json"
CERT_ERASE=ROOT/"hyp105_w34_zero_incidence_erasure_certificates.json"
RISKS={"lex":(1,475,54,25),"reverse-line":(0,61,61,26)}
SCHEMA="mathlab.hyp105.original-frozen-core-fibers.v1"
ALL_ORIGINAL=425
PHYSICAL=28


def real_source(scheme):
    if scheme not in RISKS:
        raise ValueError("only independently certified W34 original scheme")
    parent=json.loads(CERT_COVER.read_text(encoding="utf-8"))
    erase=json.loads(CERT_ERASE.read_text(encoding="utf-8"))
    z=parent["schemes"][scheme]
    r2,d3,r3,minimum=RISKS[scheme]
    if (parent["root_status"]!="OPEN_WITH_FORMAL_BLOCKER"
        or parent["actual_true_original_W34_N"]!=425
        or parent["physical_GF5_dimension"]!=28
        or z["initial_complete_D2_D3_TRUE_R3"]!=[r2,d3,r3]
        or z["transversal_certified_lower"]!=minimum
        or z["hitting_set_certified_upper"]!=minimum
        or z["bounded_exact_search_status"]!="EXACT"
        or erase["root_230_status"]!="OPEN_WITH_FORMAL_BLOCKER"
        or erase["all_h_theorem_proved"]):
        raise AssertionError("true ORIGINAL frozen parent cover not exact")
    t=tuple(z["explicit_original_ID_hitting_set"])
    if len(t)!=minimum or tuple(sorted(set(t)))!=t:
        raise AssertionError("not an exact canonical minimum source cover")
    events=z["initial_R2_true_original_signed_partitions"]+z[
        "initial_R3_true_original_signed_partitions"]
    edges=normalize_edges(tuple(a+b for a,b in events))
    if not covers(edges,t):
        raise AssertionError("certified T misses an initial ORIGINAL conflict")
    frozen_source=erase["scheme_results"][scheme]
    indices=tuple(frozen_source["original_source_425_legal_palette_indices_before"])
    model=pair_labeled_symplectic(2,scheme)
    ids,columns=exact_gf5_original_vectors(model,indices)
    if (model["s"],model["N"],model["m"])!=(4,425,28):
        raise AssertionError("not original symplectic W34")
    if ids!=tuple(range(425)) or len(columns)!=425 or len(set(columns))!=425:
        raise AssertionError("original source ID or singleton uniqueness broken")
    supports=[]
    a=model["a"]
    for flag,(p,ell) in enumerate(model["incidences"]):
        support=(model["left_labels"][p][0],
                 model["left_labels"][p][1],
                 a+model["right_labels"][ell][0],
                 a+model["right_labels"][ell][1])
        if (len(set(support))!=4 or
            tuple(columns[flag][x] for x in support)!=PALETTES[indices[flag]]):
            raise AssertionError("corrupt real physical GF5 source support")
        supports.append(support)
    return model,indices,columns,tuple(supports),t


def input_text(scheme):
    model,indices,columns,supports,t=real_source(scheme)
    lines=[f"HYP105_FROZEN_CORE_V1 {scheme} 425 28 {len(t)}"]
    for k in range(425):
        lines.append(" ".join(str(v) for v in
            (indices[k],*supports[k],*columns[k])))
    lines.extend(" ".join(map(str,p)) for p in PALETTES)
    lines.append(" ".join(map(str,t)))
    return "\n".join(lines)+"\n"


def write_input(scheme,path):
    s=input_text(scheme)
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(s,encoding="utf-8")
    return sha256(s.encode()).hexdigest()


def validate_results(scheme,data,*,shard=None,shards=None):
    model,indices,columns,supports,t=real_source(scheme)
    F=set(range(425))-set(t)
    if (data.get("schema")!=SCHEMA or data.get("scheme")!=scheme
        or data.get("n")!=425 or data.get("m")!=28
        or data.get("selected_original_ID_count")!=len(t)
        or data.get("frozen_original_ID_count")!=len(F)
        or data.get("edited_original_IDs")!=list(t)):
        raise AssertionError("incompatible full ORIGINAL frozen-core source")
    if shard is not None and (data["shard"],data["shards"])!=(shard,shards):
        raise AssertionError("incorrect source-ID shard")
    expected=tuple(i for i in t if i%data["shards"]==data["shard"])
    processed=tuple(x["source_ID"] for x in data["results"])
    if processed!=expected or len(processed)!=len(set(processed)):
        raise AssertionError("incomplete/duplicate original target IDs")
    summary=[]
    for row in data["results"]:
        i=row["source_ID"]
        if (row["frozen_pairs_processed"]!=math.comb(len(F),2) or
            row["frozen_triples_processed"]!=math.comb(len(F),3)):
            raise AssertionError("frozen physical pair/triple census incomplete")
        records=row["patterns"]
        if len(records)!=51 or tuple(p["palette"] for p in records)!=tuple(range(51)):
            raise AssertionError("not all exact 51 checksum4 source patterns")
        forbidden=set()
        for p in records:
            v=p["palette"];count2=p["R2_fixed_core_count"]
            count3=p["R3_fixed_core_count"]
            if type(count2) is not int or type(count3) is not int or min(count2,count3)<0:
                raise AssertionError("invalid signed source counts")
            bad=count2+count3>0
            if p["forbidden"] is not bad:
                raise AssertionError("incomplete forbidden palette histogram")
            if not bad:
                if any(key in p for key in
                    ("witness_k","positive_original_IDs","negative_original_IDs")):
                    raise AssertionError("unblocked source pattern has fake witness")
                continue
            forbidden.add(v)
            k=p["witness_k"]
            pos=tuple(p["positive_original_IDs"])
            neg=tuple(p["negative_original_IDs"])
            if (k not in (2,3) or len(pos)!=k or len(neg)!=k
                or pos[0]!=i or len(set(pos+neg))!=2*k
                or not (set(pos[1:]+neg)<=F)
                or (count2 if k==2 else count3)==0):
                raise AssertionError("not a disjoint frozen-original source witness")
            replacement=list(columns[i])
            for coord,x in zip(supports[i],PALETTES[v]):
                replacement[coord]=x
            for coord in range(model["m"]):
                left=(replacement[coord]+sum(columns[x][coord] for x in pos[1:]))%5
                right=sum(columns[x][coord] for x in neg)%5
                if left!=right:
                    raise AssertionError("FORBIDDEN pattern not a true physical GF5 equality")
        allowed=tuple(i for i in range(51) if i not in forbidden)
        if (len(forbidden)!=row["blocked_count"] or
            list(allowed)!=row["allowed_palettes"]):
            raise AssertionError("frozen-core source palette availability mismatch")
        summary.append((i,len(forbidden),len(allowed)))
    return summary


def aggregate(scheme,folder,out):
    _,_,_,_,t=real_source(scheme)
    files=sorted(folder.glob(f"{scheme}-*-of-*.json"))
    if not files:raise ValueError("no exact hosted frozen core shards")
    shards={}
    summaries={}
    for f in files:
        a=json.loads(f.read_text(encoding="utf-8"))
        no=a.get("shard");count=a.get("shards")
        if count!=4 or no not in range(4) or no in shards:
            raise AssertionError("wrong/incomplete actual source matrix")
        for i,bad,allowed in validate_results(scheme,a,shard=no,shards=4):
            if i in summaries:raise AssertionError("duplicate original target ID")
            summaries[i]={"forbidden_count":bad,"allowed_count":allowed}
        shards[no]=a
    if set(shards)!=set(range(4)) or set(summaries)!=set(t):
        raise AssertionError("missing exhaustive four shards of source IDs")
    dead=[i for i in t if summaries[i]["allowed_count"]==0]
    status="CERTIFIED_THIS_T_UNSAT" if dead else "ALL_SINGLE_SOURCE_DOMAINS_NONEMPTY_NOT_FEASIBILITY"
    result={
        "schema":"mathlab.hyp105.frozen-core-full-W34-summary.v1",
        "scheme":scheme,"true_W34_source_FLAGS":425,
        "GF5_physical_coordinates":28,
        "parent_721_exact_SHA":PARENT_721,
        "selected_exact_minimum_abstract_original_cover":list(t),
        "fixed_original_ID_count":425-len(t),
        "all_51_palette_domains_proved_by_exhaustive_complete_fixed_core":True,
        "result_by_original_ID":{str(i):summaries[i] for i in t},
        "empty_domain_source_IDs":dead,
        "status":status,
        "claim_about_other_minimum_source_covers":False,
        "claim_about_full_multi_source_CSP_feasibility":False,
        "claim_about_all_h_root":False,
        "root_230_status":"OPEN_WITH_FORMAL_BLOCKER",
    }
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    return result


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--scheme",choices=tuple(RISKS),required=True)
    sub=ap.add_mutually_exclusive_group(required=True)
    sub.add_argument("--prepare",type=Path)
    sub.add_argument("--verify",type=Path)
    sub.add_argument("--aggregate",type=Path)
    ap.add_argument("--out",type=Path)
    ap.add_argument("--shard",type=int)
    ap.add_argument("--shards",type=int)
    a=ap.parse_args()
    if a.prepare:
        print("AA4_W34_TRUE_ORIGINAL_FROZEN_INPUT_SHA256="+write_input(a.scheme,a.prepare))
    elif a.verify:
        j=json.loads(a.verify.read_text(encoding="utf-8"))
        result=validate_results(a.scheme,j,shard=a.shard,shards=a.shards)
        print("AA4_W34_FROZEN_CORE_WITNESSES_INDEPENDENT_PASS="+json.dumps(result))
    else:
        if a.out is None:ap.error("aggregate requires --out")
        report=aggregate(a.scheme,a.aggregate,a.out)
        print("AA4_W34_FROZEN_SOURCE_RESULT="+json.dumps(
            report,sort_keys=True,separators=(",",":")))
if __name__=="__main__":
    main()
