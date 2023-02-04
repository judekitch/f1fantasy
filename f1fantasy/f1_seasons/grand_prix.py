from functools import partial
import sys
import json
from rdflib import Graph, RDF, Literal

from f1fantasy.graph import rdf_prefix
from f1fantasy.model import gp

BAHRAIN = gp.Gp(name="Bahrain", symbolic_name="BAH")

BahrainGrandPrix = gp.Gp(name='Bahrain Grand Prix', symbolic_name='BAH')
SaudiArabianGrandPrix = gp.Gp(name='Saudi Arabian Grand Prix', symbolic_name='SAU')
AustralianGrandPrix = gp.Gp(name='Australian Grand Prix', symbolic_name='AUS')
EmiliaRomagnaGrandPrix = gp.Gp(name='Emilia Romagna Grand Prix', symbolic_name='EMR')
MiamiGrandPrix = gp.Gp(name='Miami Grand Prix', symbolic_name='MIA')
SpanishGrandPrix = gp.Gp(name='Spanish Grand Prix', symbolic_name='SPA')
MonacoGrandPrix = gp.Gp(name='Monaco Grand Prix', symbolic_name='MON')
AzerbaijanGrandPrix = gp.Gp(name='Azerbaijan Grand Prix', symbolic_name='AZB')
CanadianGrandPrix = gp.Gp(name='Canadian Grand Prix', symbolic_name='CAN')
BritishGrandPrix = gp.Gp(name='British Grand Prix', symbolic_name='GBR')
AustrianGrandPrix = gp.Gp(name='Austrian Grand Prix', symbolic_name='AUT')
FrenchGrandPrix = gp.Gp(name='French Grand Prix', symbolic_name='FRA')
HungarianGrandPrix = gp.Gp(name='Hungarian Grand Prix', symbolic_name='HUN')
BelgianGrandPrix = gp.Gp(name='Belgian Grand Prix', symbolic_name='BEL')
ItalianGrandPrix = gp.Gp(name='Italian Grand Prix', symbolic_name='ITA')
SingaporeGrandPrix = gp.Gp(name='Singapore Grand Prix', symbolic_name='SIG')
JapaneseGrandPrix = gp.Gp(name='Japanese Grand Prix', symbolic_name='JAP')
UnitedStatesGrandPrix = gp.Gp(name='United States Grand Prix', symbolic_name='USA')
MexicoCityGrandPrix = gp.Gp(name='Mexico City Grand Prix', symbolic_name='MEX')
BrazilianGrandPrix = gp.Gp(name='Brazilian Grand Prix', symbolic_name='BRA')
AbuDhabiGrandPrix = gp.Gp(name='Abu Dhabi Grand Prix', symbolic_name='ABD')
NetherlandsGrandPrix = gp.Gp(name='Netherlands Grand Prix', symbolic_name='NED')
QatarGrandPrix = gp.Gp(name='Qatar Grand Prix', symbolic_name='QAT')
LasVegasGrandPrix = gp.Gp(name='Las Vegas Grand Prix', symbolic_name='LOS')

from . import years


def gps(g: Graph):
    [add_gp_to_graph(g, prix) for prix in grand_prix_in_module()]
    [add_events_to_graph(g, year_module) for year_module in years.years]
    return g


def add_gp_to_graph(g, prix):
    g.add((prix.subject, RDF.type, rdf_prefix.fau_f1.GrandPrix))
    g.set((prix.subject, rdf_prefix.skos.notation, Literal(prix.name)))


def add_events_to_graph(g, year_module):
    return getattr(year_module, "add_events_to_graph")(g)




def grand_prix_in_module():
    return [getattr(sys.modules[__name__], name) for name in dir(sys.modules[__name__]) if 'GrandPrix' in name]
