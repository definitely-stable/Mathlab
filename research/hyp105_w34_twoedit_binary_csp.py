"""HYP-105 AA4-BINARY exact ORIGINAL W34 two-edit GF5 sector.

Reconstructs real symplectic original 425 columns with fixed globally
pair-injective f,g; independently authenticates all 25/26 one-variable
51-palette source domains against the saved full physical witnesses;
emits exact inputs for the indexed, full-GF5 C++ two-variable referee;
checks EVERY emitted pairwise forbidden original ID witness in 28D;
reconstructs complete binary compatibility and sound arc consistency.
No zero-ASET or all-h statement is inferred from nonempty AC3 domains.
"""
from collections import Counter
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import argparse
import json
import math

from hyp105_original_gf5_deterministic_extraction_referee import PALETTES
from hyp105_frozen_core_fiber import (
    real_source, validate_results, ROOT as RESEARCH_ROOT)
from hyp105_original_event_cover import covers, normalize_edges

PARENT_722="10958b04a2bd62f258b95e22f294ea222622a292"
REPORT_SCHEMA="mathlab.hyp105.original-W34-binary-sector.v1"
SUMMARY_SCHEMA="mathlab.hyp105.original-W34-2editable-binary-csp-summary.v1"


def _read_domains(scheme, directory):
    model,indices,columns,supports,T=real_source(scheme)
    parent=json.loads((RESEARCH_ROOT/
        "hyp105_w34_frozen_core_domain_certificates.json").read_text(
            encoding="utf-8"))
    if (parent["source_parent_721_exact_SHA"]!=
           "25178580d7c820bdfc0c909c4f72df70ad38d2c2"
        or parent["root_A_B_C_closed"]):
        raise AssertionError("wrong true original frozen scientific parent")
    saved=parent["schemes"][scheme]
    files=sorted(directory.glob(f"{scheme}-*-of-4.json"))
    if len(files)!=4:
        raise ValueError("all four exact frozen-core physical GF5 shards needed")
    domains={}
    for path in files:
        raw=json.loads(path.read_text(encoding="utf-8"))
        shard=raw["shard"]
        validate_results(scheme,raw,shard=shard,shards=4)
        for row in raw["results"]:
            i=row["source_ID"]
            if i in domains:raise AssertionError("duplicate edited original source")
            domains[i]=tuple(row["allowed_palettes"])
    if set(domains)!=set(T):
        raise AssertionError("missing actual min-cover source-ID frozen fibers")
    if (sum(len(x) for x in domains.values())!=
        saved["sum_allowed_p2_p3_single_source_domains"]):
        raise AssertionError("source physical domain certificate count changed")
    for i in T:
        row=next(x for x in saved["all_source_palette_local_domains"]
                 if x["source_ID"]==i)
        if len(domains[i])!=row["allowed_p2_p3"] or not domains[i]:
            raise AssertionError("true original one-edit source domain drift")
    return model,indices,columns,supports,T,domains


def binary_source_text(scheme, directory):
    model,indices,columns,supports,T,domains=_read_domains(scheme,directory)
    n=len(columns);m=model["m"]
    F=tuple(i for i in range(n) if i not in set(T))
    if n!=425 or m!=28 or len(F) not in (399,400):
        raise AssertionError("not actual full original W34 source")
    head=f"HYP105_BINARY_ORIGINAL_V1 {scheme} {n} {m} {len(T)} {len(F)}"
    lines=[head]
    for k in range(n):
        lines.append(" ".join(map(str,(indices[k],*supports[k],*columns[k]))))
    lines.extend(" ".join(map(str,p)) for p in PALETTES)
    lines.append(" ".join(map(str,T)))
    lines.append(" ".join(map(str,F)))
    lines.extend(str(sum(1<<p for p in domains[i])) for i in T)
    return "\n".join(lines)+"\n"


def prepare(scheme, fixed_core_shards, destination):
    contents=binary_source_text(scheme,fixed_core_shards)
    destination.parent.mkdir(parents=True,exist_ok=True)
    destination.write_text(contents,encoding="utf-8")
    return sha256(contents.encode("utf-8")).hexdigest()


def _recolored_column(cols,supports,i,p):
    v=list(cols[i])
    for coord,x in zip(supports[i],PALETTES[p]):
        v[coord]=x
    return tuple(v)


def validate_shard(scheme, fixed_core_shards, data, *, shard, shards):
    model,indices,columns,supports,T,domains=_read_domains(
        scheme,fixed_core_shards)
    F=tuple(i for i in range(425) if i not in set(T))
    if (data.get("schema")!=REPORT_SCHEMA
        or data.get("scheme")!=scheme
        or data.get("n")!=425 or data.get("m")!=28
        or data.get("edited_original_source_IDs")!=list(T)
        or data.get("frozen_original_source_IDs")!=list(F)
        or (data.get("shard"),data.get("shards"))!=(shard,shards)
        or data.get("all_frozen_pairs")!=math.comb(len(F),2)
        or data.get("all_frozen_triples")!=math.comb(len(F),3)):
        raise AssertionError("not complete true original GF5 source/census")
    all_pairs=list(combinations(T,2))
    expected=tuple(x for k,x in enumerate(all_pairs) if k%shards==shard)
    observed=tuple((x["source_i"],x["source_j"])
                   for x in data["results"])
    if expected!=observed:
        raise AssertionError("missing or duplicated source pair in exact shard")
    rows=[]
    for row in data["results"]:
        i=row["source_i"];j=row["source_j"]
        P=domains[i];Q=domains[j]
        if (row["domain_i"]!=len(P) or row["domain_j"]!=len(Q)
            or row["total_domain_pairs"]!=len(P)*len(Q)
            or type(row["opposite_fixed_pair_ordered_matches"]) is not int
            or row["opposite_fixed_pair_ordered_matches"]<0):
            raise AssertionError("incomplete two-editable original-source domain")
        allowed=set(tuple(x) for x in row["allowed_pairs"])
        if len(allowed)!=len(row["allowed_pairs"]):
            raise AssertionError("duplicate binary allowed tuple")
        bad=set()
        all_possible={(p,q) for p in P for q in Q}
        cols={}
        for x in (i,j):
            cols[x]={p:_recolored_column(columns,supports,x,p)
                     for p in domains[x]}
        for z in row["forbidden"]:
            p=z["p"];q=z["q"];k=z["k"]
            values=(p,q)
            if values in bad or values not in all_possible or k not in (2,3):
                raise AssertionError("bad exact binary source tuple or degree")
            bad.add(values)
            pos=tuple(z["positive_original_IDs"])
            neg=tuple(z["negative_original_IDs"])
            if (len(pos)!=k or len(neg)!=k
                or len(set(pos+neg))!=2*k
                or set(pos+neg)&set(T)!={i,j}
                or not set(pos+neg)-{i,j}<=set(F)
                or i not in pos or j not in pos+neg):
                raise AssertionError("not true 2-edit signed ORIGINAL source witness")
            for coord in range(28):
                def c(source):
                    if source==i:return cols[i][p][coord]
                    if source==j:return cols[j][q][coord]
                    return columns[source][coord]
                if sum(map(c,pos))%5!=sum(map(c,neg))%5:
                    raise AssertionError("2-edit forbidden tuple NOT full GF5^28")
        if (allowed&bad or allowed|bad!=all_possible or
            len(allowed)!=row["allowed_pairs_count"] or
            len(allowed)+len(bad)!=row["total_domain_pairs"]):
            raise AssertionError("truncated exact two-editable source pair matrix")
        rows.append((i,j,len(allowed),len(bad)))
    return rows


def exact_ac3(editable_ids,domains,allowed_pairs):
    """Deterministic arc-consistency with independent replayable deletions.

    A removed value p of i has NO support in a neighbor j's
    currently remaining domain, as shown by complete exact binary
    allowed relation. This is sound for ALL full-CSP solutions.
    """
    T=tuple(editable_ids)
    D={i:set(domains[i]) for i in T}
    relations={}
    for (i,j),pairs in allowed_pairs.items():
        if not i<j or i not in D or j not in D:
            raise ValueError("bad original source CSP edge")
        relations[(i,j)]=set(tuple(x) for x in pairs)
        relations[(j,i)]={(b,a) for a,b in pairs}
    if len(relations)!=len(T)*(len(T)-1):
        raise ValueError("binary source CSP must include EVERY variable pair")
    steps=[]
    rounds=0
    while True:
        changed=False
        for i in T:
            for p in sorted(D[i]):
                for j in T:
                    if i==j:continue
                    valid=relations[(i,j)]
                    if any((p,q) in valid for q in D[j]):
                        continue
                    steps.append({"removed_source_ID":i,"removed_palette":p,
                                  "unsupporting_neighbor_source_ID":j})
                    D[i].remove(p)
                    changed=True
                    break
        rounds+=1
        if not changed or any(not D[i] for i in T):
            break
    # Replay proof transcript against original exact relation.
    rep={i:set(domains[i]) for i in T}
    for step in steps:
        i=step["removed_source_ID"]
        p=step["removed_palette"]
        j=step["unsupporting_neighbor_source_ID"]
        if (p not in rep[i] or i==j or j not in rep or
            any((p,q) in relations[(i,j)] for q in rep[j])):
            raise AssertionError("invalid binary arc consistency deletion witness")
        rep[i].remove(p)
    if rep!=D:
        raise AssertionError("arc-consistency certificate replay drift")
    return {"domains":{str(i):sorted(D[i]) for i in T},
            "removals":steps,"rounds":rounds,
            "empty_ids":[i for i in T if not D[i]]}


def aggregate(scheme,fixed_core_shards,binary_shards,out):
    model,indices,columns,supports,T,domains=_read_domains(
        scheme,fixed_core_shards)
    files=sorted(binary_shards.glob(f"{scheme}-binary-*-of-*.json"))
    if not files:raise ValueError("missing exact binary originals")
    data={}
    summaries=[]
    for p in files:
        z=json.loads(p.read_text(encoding="utf-8"))
        shard=z.get("shard");shards=z.get("shards")
        if shard in data or shards!=4 or shard not in range(4):
            raise AssertionError("wrong full pairwise CSP matrix source sharding")
        summaries.extend(validate_shard(scheme,fixed_core_shards,z,
                                        shard=shard,shards=4))
        data[shard]=z
    if set(data)!=set(range(4)) or len(summaries)!=math.comb(len(T),2):
        raise AssertionError("missing one or more of all original binary source pairs")
    relations={}
    for k in range(4):
        for row in data[k]["results"]:
            ij=(row["source_i"],row["source_j"])
            if ij in relations:raise AssertionError("duplicate binary relation")
            relations[ij]=tuple(tuple(x) for x in row["allowed_pairs"])
    expected=set(combinations(T,2))
    if set(relations)!=expected:
        raise AssertionError("not the entire true original 25/26-source CSP graph")
    arc=exact_ac3(T,domains,relations)
    result={
        "schema":SUMMARY_SCHEMA,
        "scheme":scheme,
        "original_true_W34_N":425,
        "complete_GF5_dimension":28,
        "parent_722_exact_HEAD":PARENT_722,
        "actual_original_source_cover":list(T),
        "all_true_frozen_original_ID_count":425-len(T),
        "all_two_editable_source_pairs_checked":len(summaries),
        "all_source_domain_pair_tuples_checked":
            sum(a+b for i,j,a,b in summaries),
        "all_exact_signed_2v2_3v3_pair_tuples_surviving":
            sum(a for i,j,a,b in summaries),
        "all_exact_signed_pair_tuples_excluded":
            sum(b for i,j,a,b in summaries),
        "pairs_with_zero_valid_tuples":[[i,j] for i,j,a,b in summaries if a==0],
        "arc_consistency":arc,
        "source_singleton_frozen_domains":{
            str(i):list(domains[i]) for i in T},
        "source_pairwise_relation_sizes":{
            str(i)+","+str(j):len(relations[(i,j)])
            for i,j in sorted(relations)},
        "if_empty_domain_proves_THIS_T_unsat":True,
        "claim_about_alternative_minimum_covers":False,
        "claim_about_full_joint_source_0to3_GF5_ASET":False,
        "claim_about_all_h_seven_motifs":False,
        "root_230_status":"OPEN_WITH_FORMAL_BLOCKER",
    }
    permanent=json.loads((RESEARCH_ROOT/
        "hyp105_w34_twoedit_binary_csp_certificates.json").read_text(
            encoding="utf-8"))
    if (permanent["schema"]!=
            "mathlab.hyp105.original-W34-full-two-editable-binary-CSP-certificate.v1"
        or permanent["scientific_parent_722_exact_SHA"]!=PARENT_722
        or result!=permanent["schemes"][scheme]):
        raise AssertionError("permanent full ORIGINAL GF5 W34 two-edit CSP source certificate drift")
    print("AA4_PERMANENT_EXACT_GF5_BINARY_CSP_REPLAY_PASS="+scheme)
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",
                   encoding="utf-8")
    return result


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--scheme",choices=("lex","reverse-line"),required=True)
    p.add_argument("--frozen",type=Path,required=True)
    sub=p.add_mutually_exclusive_group(required=True)
    sub.add_argument("--prepare",type=Path)
    sub.add_argument("--verify",type=Path)
    sub.add_argument("--aggregate",type=Path)
    p.add_argument("--out",type=Path)
    p.add_argument("--shard",type=int)
    p.add_argument("--shards",type=int)
    args=p.parse_args()
    if args.prepare:
        print("AA4_BINARY_TRUE_ORIGINAL_SOURCE_INPUT_SHA256="+
              prepare(args.scheme,args.frozen,args.prepare))
    elif args.verify:
        z=json.loads(args.verify.read_text(encoding="utf-8"))
        rows=validate_shard(args.scheme,args.frozen,z,shard=args.shard,
                            shards=args.shards)
        print("AA4_BINARY_GF5_28D_ORIGINAL_SIGNED_WITNESS_PASS="+
              json.dumps(rows,separators=(",",":")))
    else:
        if args.out is None:p.error("--aggregate needs --out")
        z=aggregate(args.scheme,args.frozen,args.aggregate,args.out)
        print("AA4_BINARY_CSP_EXACT_RESULT="+json.dumps(
            z,sort_keys=True,separators=(",",":")))
if __name__=="__main__":
    main()
