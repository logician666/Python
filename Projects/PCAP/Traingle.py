import Points_on_a_Plan
Point = Points_on_a_Plan.Point

class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__vertices = [vertice1, vertice2, vertice3]


    def perimeter(self):
        return self.__vertices[0].distance_from_point(self.__vertices[1]) + \
                self.__vertices[1].distance_from_point(self.__vertices[2]) + \
                self.__vertices[2].distance_from_point(self.__vertices[0])


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
