"""C24-B8-H independent finite global-injection cylinder tests (no real GQ here)."""
from itertools import combinations,permutations
import unittest

from hyp105_g5e2b3e1c24b8h_joint_source_cylinder import (
    falling,validate_problem,joint_cylinder_certificate,
)

EDGES=tuple(combinations(range(4),2))


def toy_source():
    """Nonlinear intersection events, one global K4 edge injection."""
    records=[]
    for i,j in combinations(range(4),2):
        records.append(((i,j),(i+j)%3+1,(i,j,"adjacent")))
        records.append(((i,j),(i*j)%4+1,(i,j,"disjoint")))
    for i,j,k in combinations(range(4),3):
        records.append(((i,j,k),2,(i,j,k,"triangle")))
    return tuple(records)


def physical_accept(payload,assignment):
    *ids,kind=payload
    es=[EDGES[assignment[i]] for i in ids]
    adjacent=lambda a,b:bool(set(a)&set(b))
    if kind=="adjacent":
        return adjacent(es[0],es[1])
    if kind=="disjoint":
        return not adjacent(es[0],es[1])
    return (adjacent(es[0],es[1]) and
            adjacent(es[0],es[2]) and adjacent(es[1],es[2]))


def independently_brute(records,pinned):
    free=tuple(i for i in range(4) if i not in pinned)
    available=tuple(i for i in range(6) if i not in pinned.values())
    scores=[]
    for images in permutations(available,len(free)):
        assignment={**pinned,**dict(zip(free,images))}
        scores.append(sum(w*physical_accept(payload,assignment)
                          for _,w,payload in records))
    return min(scores),max(scores),len(scores)


class JointCylinderTests(unittest.TestCase):
    def test_all_k4_global_pins_and_coupled_lower(self):
        records=toy_source()
        for pins in ({},{0:0},{0:0,1:1},{0:3,1:2,2:0}):
            free=4-len(pins)
            expected,_,states=independently_brute(records,pins)
            result=joint_cylinder_certificate(
                records,pins,4,6,physical_accept,
                max_union_support=min(3,free),
                max_group_states=1000)
            self.assertEqual(result["exact_cylinder_minimum"],expected)
            self.assertEqual(result["whole_completion_states_evaluated"],states)
            self.assertLessEqual(result["supportwise_pointwise_seven_lower"],
                                 result["coupled_pointwise_seven_lower"])
            self.assertLessEqual(result["coupled_pointwise_seven_lower"],expected)
            self.assertEqual(result["original_source_records"],len(records))

    def test_exact_original_multiplicity_and_partial_support(self):
        records=(((0,1),7,(0,1,"adjacent")),
                 ((0,1),3,(0,1,"disjoint")))
        for e0,e1 in permutations(range(6),2):
            pin={0:e0,1:e1}
            direct=7 if bool(set(EDGES[e0])&set(EDGES[e1])) else 3
            result=joint_cylinder_certificate(
                records,pin,4,6,physical_accept,
                max_union_support=2,max_group_states=200)
            self.assertEqual(result["supportwise_pointwise_seven_lower"],direct)
            self.assertEqual(result["coupled_pointwise_seven_lower"],direct)
            self.assertEqual(result["exact_cylinder_minimum"],direct)

    def test_fall_back_without_exact_is_certified(self):
        records=toy_source()
        no_exact=joint_cylinder_certificate(
            records,{0:0},4,6,physical_accept,
            max_union_support=2,include_exact=False,max_group_states=1000)
        self.assertIsNone(no_exact["exact_cylinder_minimum"])
        self.assertLessEqual(no_exact["coupled_pointwise_seven_lower"],
                             independently_brute(records,{0:0})[0])
        self.assertEqual(falling(6,4),360)

    def test_fail_closed_invalid_global_maps_sources_and_budgets(self):
        records=toy_source()
        with self.assertRaises(ValueError):
            validate_problem(records,{0:0,1:0},4,6)
        with self.assertRaises(ValueError):
            validate_problem(records,{0:0,4:1},4,6)
        with self.assertRaises(ValueError):
            validate_problem([((1,0),1,None)],{},4,6)
        with self.assertRaises(ValueError):
            validate_problem([((0,1),0,None)],{},4,6)
        with self.assertRaises(ValueError):
            joint_cylinder_certificate(records,{},4,6,physical_accept,
                                       max_union_support=3,max_group_states=1)
        with self.assertRaises(ValueError):
            joint_cylinder_certificate(records,{},4,6,physical_accept,
                                       max_union_support=3,
                                       max_record_evaluations=1)
        with self.assertRaises(ValueError):
            joint_cylinder_certificate(records,{},4,6,
                                       lambda payload,assign:2,
                                       max_union_support=3)
        with self.assertRaises(ValueError):
            joint_cylinder_certificate(records,{},4,6,physical_accept,
                                       max_union_support=5)

if __name__=="__main__":
    unittest.main()
