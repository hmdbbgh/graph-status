from igraph import Graph

import plotly.graph_objects as go


class DrawGraph:


    # Initialize the class
    def __init__(self, graph, axis_flag = False):

        self.graph = graph

        self.axis_flag = axis_flag

        self.num_of_vertics = graph.get_num_of_vertices()

        self.create_graph()


    def create_graph(self):

        self.G = Graph.Tree(self.num_of_vertics, 2)         # 2 stands for children number

        self.lay = self.G.layout('rt')

        self.create_vertics()

        self.create_edges()
        

    def create_vertics(self):

        self.vertics_label = list(map(str, range(self.num_of_vertics)))

        self.determine_vertices_position()


    def determine_vertices_position(self):

        self.position = {vertice: self.lay[vertice] for vertice in range(self.num_of_vertics)}
        
        self.M = max([self.lay[vertice][1] for vertice in range(self.num_of_vertics)])
        
        self.Xn = [self.position[pos][0] for pos in range(len(self.position))]

        self.Yn = [2 * self.M-self.position[pos][1] for pos in range(len(self.position))]


    def create_edges(self):

        vertices = self.graph.get_vertices()

        self.edges = list()

        for vertice in vertices:

            self.edges += [(vertice, neighbor) for neighbor in self.graph.get_neighbors(vertice)]

        print('Edges: {}'.format(self.edges))

        self.determine_edges_position()


    def determine_edges_position(self):

        self.Xe = []    # X of edges

        self.Ye = []    # Y of edges

        for edge in self.edges:
            
            self.Xe+=[self.position[edge[0]][0],self.position[edge[1]][0], None]

            self.Ye+=[2*self.M-self.position[edge[0]][1],2*self.M-self.position[edge[1]][1], None]


    def make_annotations(self, font_size=10, font_color='rgb(250,250,250)'):

        if len(self.vertics_label) != len(self.position):

            raise ValueError('The lists positions and labels must have the same len')

        annotations = []

        for k in range(len(self.position)):

            annotations.append(

                dict(

                    text = self.vertics_label[k],

                    x = self.position[k][0],
                    
                    y = 2 * self.M-self.position[k][1],

                    xref = 'x1',
                    
                    yref = 'y1',

                    font = dict(color = font_color, size = font_size),

                    showarrow = False
                )
            )

        return annotations


    def draw(self):

        fig = go.Figure()

        fig.add_trace(                                 # add lines between nodes

                go.Scatter(

                        x = self.Xe,

                        y = self.Ye,

                        mode = 'lines',

                        line = dict(color = 'rgb(210,210,210)', width = 1),

                        hoverinfo = 'none'
                    )
            )

        fig.add_trace(                                  # add texts for nodes

                go.Scatter(

                        x = self.Xn,

                        y = self.Yn,

                        mode = 'markers',

                        name = 'bla',

                        marker = dict(

                                    symbol = 'circle-dot',

                                    size = 18,

                                    color = '#6175c1',    #'#DB4551', red color

                                    line = dict(color = 'rgb(50,50,50)', width = 1)
                                ),

                        text = self.vertics_label,

                        hoverinfo = 'text',

                        opacity = 0.8
                    )
            )

        axis = dict(                                     # False axis if axis_flag is Flase otherwise True

                    showline = False if not self.axis_flag else True,

                    zeroline = False if not self.axis_flag else True,

                    showgrid = False if not self.axis_flag else True,

                    showticklabels = False if not self.axis_flag else True,
                )

        fig.update_layout(

                    title = 'Graph',

                    annotations = self.make_annotations(),

                    font_size = 12,

                    showlegend = False,

                    xaxis = axis,

                    yaxis = axis,

                    margin = dict(l = 40, r = 40, b = 85, t = 100),

                    hovermode = 'closest',

                    plot_bgcolor = 'rgb(248,248,248)'
                )

        fig.show()