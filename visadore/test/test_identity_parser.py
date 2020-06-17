from hypothesis import given
from hypothesis.strategies import text, characters
from visadore.identity import Identity
from visadore.identity import _identity_parser


def make_identity_string(company, model, serial, config):
    return ",".join([company, model, serial, config])


@given(
    text(alphabet=characters(blacklist_categories=["Cs"], blacklist_characters=[","])),
    text(alphabet=characters(blacklist_categories=["Cs"], blacklist_characters=[","])),
    text(alphabet=characters(blacklist_categories=["Cs"], blacklist_characters=[","])),
    text(alphabet=characters(blacklist_categories=["Cs"], blacklist_characters=[","])),
)
def test_identity_parser(company, model, serial, config):
    identity_nt = Identity(company, model, serial, config)
    identity_str = make_identity_string(company, model, serial, config)
    assert _identity_parser(identity_str) == identity_nt
