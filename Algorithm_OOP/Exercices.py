"""
1. Write the factorial function f(n)=n! as a recursive function.
2. Would memoization make this function faster?
3. Now what if we needed to calculate the factorial often
    (perhaps we were computing probabilities of different selections), would memoization be useful in this case?
"""


def factorial(number):
    fact = 1
    if number == 0:
        return fact
    else:
        fact = factorial(number - 1)
    fact = fact * number
    return fact


# assert factorial(1) == 1
# assert factorial(2) == 2
# assert factorial(3) == 6
# assert factorial(6) == 720
# assert factorial(10) == 3628800
# assert factorial(25) == 15511210043330985984000000

"""
Exercise 1: point_repr

The first step in defining most classes is to define their __init__ and __repr__ methods 
so that we can construct and represent distinct objects of that class. 
Our Point class should accept two arguments, x and y, 
and be represented by a string 'Point(x, y)' with appropriate values for x and y.

When you've written a Point class capable of this, execute the cell with grader.score for this question 
(do not edit that cell; you only need to modify the Point class).


Exercise 2: add_subtract

The most basic vector operations we want our Point object to handle are addition and subtraction. 
For two points  (x1,y1)+(x2,y2)=(x1+x2,y1+y2)(x1,y1)+(x2,y2)=(x1+x2,y1+y2)  and similarly for subtraction. 
Implement a method within Point that allows two Point objects to be added together using the + operator, 
and likewise for subtraction. Once this is done, execute the grader.score cell for this question 
(do not edit that cell; you only need to modify the Point class.)

(Remember that __add__ and __sub__ methods will allow us to use the + and - operators.)


Exercise 3: multiplication

Within linear algebra there's many different kinds of multiplication: 
    scalar multiplication, 
    inner product, 
    cross product, 
    and matrix product. 
We're going to implement scalar multiplication and the inner product.

We can define scalar multiplication given a point  P  and a scalar  a  as
aP=a(x,y)=(ax,ay)

and we can define the inner product for points  P,Q  as
P⋅Q=(x1,y1)⋅(x2,y2)=x1x2+y1y2
 
To test that you've implemented this correctly, compute  2(x,y)⋅(x,y)  for a Point object. 
Once this is done, execute the grader.score cell for this question 
(do not edit that cell; you only need to modify the Point class.)

(Remember that __mul__ method will allow us to use the * operator. 
Also don't forget that the ordering of operands matters when implementing these operators.)


Exercise 4: Distance

Another quantity we might want to compute is the distance between two points.
This is generally given for points  P1=(x1,y1)  and  P2=(x2,y2)  as
D=|P2−P1|= sqrt((x1−x2)^2+(y1−y2)^2)
 
Implement a method called distance which finds the distance from a point to another point.

Once this is done, execute the grader.score cell for this question 
(do not edit that cell; you only need to modify the Point class.)

Hint
    You can use the sqrt function from the math package.
    

Exercise 5: Algorithm

Now we will use these points to solve a real world problem! 
We can use our Point objects to represent measurements of two different quantities 
(e.g. a company's stock price and volume). 
One thing we might want to do with a data set is to separate the points into groups of similar points. 
Here we will implement an iterative algorithm to do this which will be a specific case of the very general  
k-means clustering algorithm. 
The algorithm will require us to keep track of two clusters, each of which have a list of points and a center 
(which is another point, not necessarily one of the points we are clustering). 
After making an initial guess at the center of the two clusters,  C1  and  C2 , the steps proceed as follows

Assign each point to  C1  or  C2  based on whether the point is closer to the center of  C1  or  C2 .
Recalculate the center of  C1  and  C2  based on the contained points. The mean from the points (mean from all x's and all y's)

See 'https://en.wikipedia.org/wiki/K-means_clustering#Standard_algorithm' for more information.

This algorithm will terminate in general when the assignments no longer change. 
For this question, we would like you to initialize one cluster at (1, 0) and the other at (-1, 0).

The returned values should be the two centers of the clusters ordered by greatest x value. 
Please return these as a list of numeric tuples  [(x1,y1),(x2,y2)] 

In order to accomplish this we will create a class called cluster which has two methods besides __init__ 
which you will need to write. The first method update will update the center of the Cluster given the 
points contained in the attribute points. Remember, you after updating the center of the cluster, 
you will want to reassign the points and thus remove previous assignments. 
The other method add_point will add a point to the points attribute.

Once this is done, execute the grader.score cell for this question (do not edit that cell; 
you only need to modify the Cluster class and compute_result function.)
"""

from math import sqrt


class Point(object):

    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def __repr__(self):
        return "Point({}, {})".format(self.X, self.Y)

    def __add__(self, pnt):
        x = self.X + pnt.X
        y = self.Y + pnt.Y
        return Point(x, y)

    def __sub__(self, pnt):
        x = self.X - pnt.X
        y = self.Y - pnt.Y
        return Point(x, y)

    def __mul__(self, q):
        if type(q) == int:
            x = self.X * q
            y = self.Y * q
            return Point(x, y)
        elif type(q) == Point:
            x = self.X * q.X
            y = self.Y * q.Y
            return x + y
        return 0

    def distance(self, q_point):
        return sqrt((self.X - q_point.X) ** 2 + (self.Y - q_point.Y) ** 2)


p = Point(3, 8)
assert p.__str__() == "Point(3, 8)"

pa = Point(2, 2)
ps = Point(1, 1)
ap = p + pa
sp = p - ps
assert ap.__str__() == "Point(5, 10)"
assert sp.__str__() == "Point(2, 7)"

smp = p * 2
assert smp.__str__() == "Point(6, 16)"

ipp = p * Point(3, 3)
assert ipp == 33

assert p.distance(pa) == 6.082762530298219


class Cluster(object):
    def __init__(self, x, y):
        self.center = Point(x, y)
        self.points = []

    def update(self):
        mean_point = Point(0, 0)
        for point in self.points:
            mean_point += point
        mean_x = int(mean_point.X / len(self.points))
        mean_y = int(mean_point.Y / len(self.points))
        self.center = Point(mean_x, mean_y)
        self.points = []

    def add_point(self, point):
        self.points.append(point)


def compute_result(points):
    # points = [Point(*point) for point in points]
    a = Cluster(1, 0)
    b = Cluster(-1, 0)
    a_old = []
    for _ in range(10000):  # max iterations
        for point in points:
            if point.distance(a.center) < point.distance(b.center):
                a.add_point(point)
            else:
                b.add_point(point)
        if a_old == a.points:
            break
        a_old = a.points
        a.update()
        b.update()
    # return [(x, y)] * 2
    print(a.points)
    print(b.points)
    return [(a.center.X, a.center.Y), (b.center.X, b.center.Y)]


points = [Point(1, 2), Point(2, 3), Point(3, 4), Point(-1, -2), Point(-2, -3), Point(-3, -4)]

clusters = compute_result(points)
print(clusters)
