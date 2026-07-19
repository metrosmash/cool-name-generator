 
import random
import name_utils as nu

def _generate_unique_names(sep:str, uname:str)-> str:
    predicate = random.choice(nu._GENERATOR_PREDICATES).lower()
    noun = uname.lower()

    return f"{predicate}{sep}{noun}"

def _generate_unique_name(uname:str, sep:str ="-", max_length:int = 20):
    """Helper function for generating a Unique name along with the name added 

    Args:
        sep: String separator for word spacing.
        max_length: Maximum allowable string length.

    Returns:
        A random string phrase comprised of a predicate and a user_input

    """
    name = None
    for _ in range(10):
        name = _generate_unique_names(sep, uname)
        if len(name) <= max_length:
            return name
    # If the combined length isn't below the threshold after 10 iterations, truncate it.
    return name[:max_length]

name = input("What name would you like Uniquefied? ")
print(_generate_unique_name(name))