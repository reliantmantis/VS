import csv
from Graph_class import *
from Vertex_class import *

def airport_departures(file):
    airports = set()
    airports_graph = Graph()
    flights = []
    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')
        for row in reader:
            airport1, airport2 = row
            airports.add(airport1)
            airports.add(airport2)
            flights.append([airport1, airport2])

    for airport in airports:
        vertex = Vertex(airport)
        airports_graph.add_vertex(vertex)
    
    for flight in flights:
        airport1, airport2 = flight
        
        # Crear instancias de Vertex si no existen
        if airport1 not in airports_graph.graph_dict:
            airports_graph.add_vertex(Vertex(airport1))
        if airport2 not in airports_graph.graph_dict:
            airports_graph.add_vertex(Vertex(airport2))
        
        # Añadir la arista
        from_vertex = airports_graph.graph_dict[airport1]
        to_vertex = airports_graph.graph_dict[airport2]
        airports_graph.add_edge(from_vertex, to_vertex)
    
    return airports_graph







airports_departures = airport_departures("C:\\Users\\carlo\\OneDrive\\Escritorio\\VS files\\CodeCademy\\Computer science\\Trees and graphs\\Portfolio project\\my_routes_no_w.csv")

print(airports_departures.graph_dict)

