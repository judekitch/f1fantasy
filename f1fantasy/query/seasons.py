from typing import List, Tuple, Union, Any
from functools import partial
from rdflib import Graph, RDF, URIRef

from f1fantasy import rdf, model, repo


def find_gp_by_symbol(g: Graph, symbol: str, to_model: bool) -> Union[Tuple, Any]:
    result = _single_result_or_none(rdf.query(g, repo.gp_by_symbol_query(symbol)))
    if not to_model:
        return result
    sub, name, label = result
    return model.Gp(subject=sub, name=name, symbolic_name=symbol, label=label)


def find_season_by_year(g: Graph, year: int, to_model: bool = False) -> Tuple:
    result = _single_result_or_none(rdf.query(g, repo.season_by_year_query(year)))
    if not to_model:
        return result

    sub, = result
    return model.Season(subject=sub, year=year)


def all_seasons(g: Graph):
    return [partial(_season_year, g)(subject) for subject, _, _ in _all_season_types(g)]


def all_gps(g: Graph):
    return [partial(_gp_symbol, g)(subject) for subject, _, _ in _all_gp_types(g)]


def _season_year(g: Graph, sub: URIRef):
    _, _, yr = rdf.first_matching_triple(g, (sub, rdf.P.fau_f1.forYear, None))
    return yr.toPython()


def _gp_symbol(g: Graph, sub: URIRef):
    _, _, symb = rdf.first_matching_triple(g, (sub, rdf.P.fau_f1.hasSymbol, None))
    return symb.toPython()


def _all_season_types(g) -> List[Tuple]:
    return rdf.all_matching_triples(g, (None, RDF.type, rdf.P.fau_f1.Season))


def _all_gp_types(g) -> List[Tuple]:
    return rdf.all_matching_triples(g, (None, RDF.type, rdf.P.fau_f1.GrandPrix))


def _single_result_or_none(result):
    result_list = list(result)
    if len(result_list) != 1:
        return None
    return result_list[0]
