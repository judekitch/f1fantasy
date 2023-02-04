from rdflib import RDF

from f1fantasy.f1_seasons import fantasy_scoring
from f1fantasy.graph import rdf_prefix
from f1fantasy.repo import triples, gn


def test_add_event_points_to_graph(init_repo, empty_graph):
    g = triples.save(fantasy_scoring.scoring(empty_graph))

    pt_triples = gn.all_matching_triples(g, (None, RDF.type, rdf_prefix.fau_f1.FantasyEventScore))

    expected_points_subs = {'https://fauve.io/fantasyTeam/TeamClojo/EventScore/BAH-2023'}

    pt_subjects = {s.toPython() for s, _, _ in pt_triples}

    assert pt_subjects == expected_points_subs
