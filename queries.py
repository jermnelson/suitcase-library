NAMESPACES = """PREFIX bf: <http://id.loc.gov/ontologies/bibframe/>
PREFIX bflc: <http://id.loc.gov/ontologies/bflc/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
"""

BOOKS = NAMESPACES + """

SELECT ?book ?label ?author
WHERE {
  ?book a bf:Text  .
  ?book rdfs:label ?label .
  ?book bf:contribution ?contrib .
  OPTIONAL {
    ?contrib a bflc:PrimaryContribution .
    ?contrib bf:agent ?agent .
    ?agent rdfs:label ?author .
  }
  OPTIONAL {
    ?contrib a bf:Contribution .
    ?contrib bf:agent ?agent .
    ?agent rdfs:label ?author .
  }
} ORDER BY ?label
"""