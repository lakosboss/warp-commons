"""Exact angular-moment check for OPH FZ-11 and FZ-12; requires SymPy."""
from itertools import combinations, product
from sympy import Poly, QQ, Rational as Q, expand, sqrt, symbols

root = sqrt(5)
phi = (1+root)/2
field = QQ.algebraic_field(root)
x, y, z = symbols("x y z")
r2 = x*x+y*y+z*z


def poly(value):
    return Poly(expand(value), x, y, z, domain=field)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def check():
    # Independent construction using cyclic permutations of the icosahedron.
    vertices = []
    for a,b in product((-1,1), repeat=2):
        seed = (0,a,b*phi)
        vertices.extend(seed[i:]+seed[:i] for i in range(3))
    unscaled_edges = []
    for v,w in combinations(vertices, 2):
        diff = [b-a for a,b in zip(v,w)]
        if expand(sum(a*a for a in diff)-4) == 0:
            unscaled_edges.append(diff)
    require(len(vertices)==12 and len(unscaled_edges)==30, "wrong orbit size")

    def moment(orbit, n, squared_norm):
        return sum(poly(sum(t*c for t,c in zip((x,y,z),v)))**n
                   for v in orbit).mul_ground(field.from_sympy(squared_norm**(-Q(n,2))))

    v2,v4,v6 = [moment(vertices,n,2+phi) for n in (2,4,6)]
    e2,e4,e6 = [moment(unscaled_edges,n,4) for n in (2,4,6)]
    require(v2 == poly(4*r2) and e2 == poly(10*r2), "quadratic moments")
    require(v4 == poly(Q(12,5)*r2**2) and e4 == poly(6*r2**2), "quartic moments")
    # Homogenize I6: its directional value is one on all vertex axes.
    i6 = (v6-poly(Q(12,7)*r2**3)).mul_ground(field.from_sympy(Q(175,64)))
    ix = (0, 1, phi)
    require(expand(i6.as_expr().subs(dict(zip((x,y,z),ix)))-(2+phi)**3) == 0,
            "wrong normalization on the vertex")
    require(i6.diff((x,2))+i6.diff((y,2))+i6.diff((z,2)) == poly(0),
            "sixth-order remainder is not harmonic")
    require(e6 == poly(Q(30,7)*r2**3)-i6.mul_ground(field.from_sympy(Q(2,7))),
            "edge sextic polynomial mismatch")

    # Normalize the cosine symbols to unit k²; include the 1/24 and 1/720.
    for label, normalization, quartic, sextic0, sextic6 in (
        ("FZ-11", Q(1,2), Q(12,5), Q(12,7), Q(64,175)),
        ("FZ-12", Q(1,5), Q(6), Q(30,7), -Q(2,7)),
    ):
        c4 = -normalization*quartic/24
        b0 = normalization*sextic0/720
        b6 = normalization*sextic6/720
        print(f"{label}: C4/a²={c4}, B0/a⁴={b0}, B6/a⁴={b6}, "
              f"B0/C4²={b0/c4**2}, B6/C4²={b6/c4**2}, B6/B0={b6/b0}")


if __name__=="__main__":
    check()
