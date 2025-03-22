from dataclasses import dataclass
from typing import Dict

@dataclass
class ClassInfo:
    rooms: Dict[str, int]

@dataclass
class DegreePlan:
    name: str
    classes: Dict[str, ClassInfo]

def get_degree_class_data():
    MEEN = DegreePlan(
        name="MEEN",
        classes={
            "PHYS 216": ClassInfo(rooms={"MPHY": 10, "BLOC": 12, "HELD": 28}),
            "ENGR 102": ClassInfo(rooms={"ZACH": 28, "BLOC": 0, "ILCB": 31}),
            "MEEN 225": ClassInfo(rooms={"ZACH": 40, "JCAIN": 28}),
        }
    )

    CHEM = DegreePlan(
        name="CHEM",
        classes={
            "PHYS 216": ClassInfo(rooms={"MPHY": 10, "BLOC": 12, "HELD": 28}),
            "CHEM 120": ClassInfo(rooms={"CHEM": 110, "HELD": 28, "HEB": 7}),
            "CHEM 228": ClassInfo(rooms={"ILCB": 210, "CHEM": 20}),
        }
    )

    CSCE = DegreePlan(
        name="CSCE",
        classes={
            "MATH 304": ClassInfo(rooms={"HEB": 22, "BLOC": 10}),
            "ENGR 102": ClassInfo(rooms={"ZACH": 28, "BLOC": 0, "ILCB": 31}),
            "CSCE 221": ClassInfo(rooms={"ILCB": 30, "PETI": 50}),
        }
    )

    return {"MEEN": MEEN, "CHEM": CHEM, "CSCE": CSCE}

