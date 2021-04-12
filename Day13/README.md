In this Bite we compare two list objects for equality, a fundamental thing to understand in Python.

Complete the check_equality function returning the various Enum values (representing equality scores) according to the type of equality of the lists:

        return SAME_REFERENCE if both lists reference the same object,
        return SAME_ORDERED if they have the same content and order,
        return SAME_UNORDERED if they have the same content unordered,
        return SAME_UNORDERED_DEDUPED if they have the same unordered content and reduced to unique items,

and finally return NO_EQUALITY if none of the previous cases match.

Note that == and is are not the same in Python!

Have fun and keep calm and code in Python!

