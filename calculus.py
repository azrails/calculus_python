from figures import volume, flat
import tkinter as tk


class VolumeF(tk.Toplevel):
    figures = ['Sphere', 'Cube', 'Parallelepiped', 'Cylinder', 'Cone', 'CorrectPyramid']

    def __init__(self, parent):
        super().__init__(parent)
        figures = {'Sphere': self.spher_calc, 'Cube': self.cube_calc, 'Parallelepiped': self.parallelepiped_calc, \
                    'Cylinder': self.cylinder_calc, 'Cone': self.cone_calc, 'CorrectPyramid': self.correct_pyramid_calc}
        self.title("Плоские фигуры")
        self.flatframe = tk.Frame(self)
        r = 0
        c = 0
        k = 0
        for i, j in figures.items():
            if k % 3 == 0 and k != 0:
                c = 0
                r += 1
            tk.Button(text=i, width=30, height=10, bg='grey', fg='black', master=self.flatframe, command=j).grid(row=r, column=c)
            c += 1
            k += 1
        self.flatframe.pack()

    def spher_calc(self) -> None:
        sp = TkSphere(self)
        sp.grab_set()

    def cube_calc(self) -> None:
        cb = TkCube(self)
        cb.grab_set()

    def parallelepiped_calc(self) -> None:
        pd = TkParallelepiped(self)
        pd.grab_set()

    def cylinder_calc(self) -> None:
        cl = TkCylinder(self)
        cl.grab_set()

    def cone_calc(self) -> None:
        cn = TkCone(self)
        cn.grab_set()

    def correct_pyramid_calc(self) -> None:
        cpd = TkCorrectPyramid(self)
        cpd.grab_set()


class TkCorrectPyramid(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.pyramidframe = tk.Frame(self)
        self.triangleresults = tk.Label(text="Results", height=3, master=self.pyramidframe).grid(row=3, column=1, padx=5, pady=5)
        self.trianglebutton = tk.Button(master=self.pyramidframe, text='Ok', width=10, height=3, command=self.calculus).grid(row=0, column=2, padx=5, pady=5)

        self.ns = tk.StringVar()
        self.trianglelable_a = tk.Label(text="Enter number of sides",  height=3, fg='black',  master=self.pyramidframe).grid(row=0, column=0, padx=5, pady=5)
        self.triangleentry_a = tk.Entry(master=self.pyramidframe, width=10, textvariable=self.ns).grid(row=0, column=1, padx=5, pady=5)

        self.s = tk.StringVar()
        self.trianglelable_b = tk.Label(text="Enter side",  height=3, fg='black',  master=self.pyramidframe).grid(row=1, column=0, padx=5, pady=5)
        self.triangleentry_b = tk.Entry(master=self.pyramidframe, width=10, textvariable=self.s).grid(row=1, column=1, padx=5, pady=5)

        self.h = tk.StringVar()
        self.trianglelable_c = tk.Label(text="Enter hieght",  height=3, fg='black',  master=self.pyramidframe).grid(row=2, column=0, padx=5, pady=5)
        self.triangleentry_c = tk.Entry(master=self.pyramidframe, width=10, textvariable=self.h).grid(row=2, column=1, padx=5, pady=5)

        self.pyramidframe.pack()

        self.si_a = tk.Label(text="Side: ",  height=3, fg='black',  master=self.pyramidframe).grid(row=4, column=0, padx=5, pady=5)
        self.sa = tk.StringVar()
        self.r_sa = tk.Label(textvariable=self.sa,  height=3, fg='black',  master=self.pyramidframe).grid(row=4, column=1, padx=5, pady=5)
        self.si_n = tk.Label(text="Number of sides: ",  height=3, fg='black',  master=self.pyramidframe).grid(row=5, column=0, padx=5, pady=5)
        self.sn = tk.StringVar()
        self.r_sn = tk.Label(textvariable=self.sn,  height=3, fg='black',  master=self.pyramidframe).grid(row=5, column=1, padx=5, pady=5)
        self.si_h = tk.Label(text="Hieght: ",  height=3, fg='black',  master=self.pyramidframe).grid(row=6, column=0, padx=5, pady=5)
        self.sh = tk.StringVar()
        self.r_sh = tk.Label(textvariable=self.sh,  height=3, fg='black',  master=self.pyramidframe).grid(row=6, column=1, padx=5, pady=5)

        self.si_apotheme = tk.Label(text="Apotheme: ",  height=3, fg='black',  master=self.pyramidframe).grid(row=7, column=0, padx=5, pady=5)
        self.ap = tk.StringVar()
        self.r_apo = tk.Label(textvariable=self.ap,  height=3, fg='black',  master=self.pyramidframe).grid(row=7, column=1, padx=5, pady=5)

        self.si_area = tk.Label(text="Area: ",  height=3, fg='black',  master=self.pyramidframe).grid(row=8, column=0, padx=5, pady=5)
        self.ar = tk.StringVar()
        self.r_ar = tk.Label(textvariable=self.ar,  height=3, fg='black',  master=self.pyramidframe).grid(row=8, column=1, padx=5, pady=5)

        self.si_volume = tk.Label(text="Volume: ",  height=3, fg='black',  master=self.pyramidframe).grid(row=9, column=0, padx=5, pady=5)
        self.vl = tk.StringVar()
        self.r_vol = tk.Label(textvariable=self.vl,  height=3, fg='black',  master=self.pyramidframe).grid(row=9, column=1, padx=5, pady=5)

        self.si_larea = tk.Label(text="Lateral area: ",  height=3, fg='black',  master=self.pyramidframe).grid(row=10, column=0, padx=5, pady=5)
        self.lar = tk.StringVar()
        self.r_lar = tk.Label(textvariable=self.lar,  height=3, fg='black',  master=self.pyramidframe).grid(row=10, column=1, padx=5, pady=5)

    def calculus(self):
        try:
            cpd = volume.CorrectPyramid(int(self.ns.get()), int(self.s.get()), int(self.h.get()))
            self.sa.set(cpd.side)
            self.sn.set(cpd.number_of_sides)
            self.sh.set(cpd.hieght)
            self.ap.set(cpd._apothem())
            self.ar.set(cpd.area())
            self.vl.set(cpd.volume())
            self.lar.set(cpd.lateral_area())
        except ValueError:
            pass


class TkCone(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.coneframe = tk.Frame(self)
        self.circlelable = tk.Label(text="Enter radius",  height=3, fg='black',  master=self.coneframe).grid(row=0, column=0, padx=5, pady=5)
        self.circleresults = tk.Label(text="Results",  height=3, master=self.coneframe).grid(row=2, column=1, padx=5, pady=5)
        self.re = tk.StringVar()
        self.circleentry = tk.Entry(master=self.coneframe, width=10, textvariable=self.re).grid(row=0, column=1, padx=5, pady=5)
        self.circlebutton = tk.Button(master=self.coneframe, text='Ok', width=10, height=3, command=self.calculus).grid(row=0, column=2, padx=5, pady=5)
        self.circlelable = tk.Label(text="Enter hieght",  height=3, fg='black',  master=self.coneframe).grid(row=1, column=0, padx=5, pady=5)
        self.h = tk.StringVar()
        self.circleentry = tk.Entry(master=self.coneframe, width=10, textvariable=self.h).grid(row=1, column=1, padx=5, pady=5)
        self.coneframe.pack()

        self.cl_radius = tk.Label(text="Radius: ",  height=3, fg='black',  master=self.coneframe).grid(row=3, column=0, padx=5, pady=5)
        self.rad = tk.StringVar()
        self.cl_rad = tk.Label(textvariable=self.rad,  height=3, fg='black',  master=self.coneframe).grid(row=3, column=1, padx=5, pady=5)
        self.cl_height = tk.Label(text="Height: ",  height=3, fg='black',  master=self.coneframe).grid(row=4, column=0, padx=5, pady=5)
        self.he = tk.StringVar()
        self.cl_hgt = tk.Label(textvariable=self.he,  height=3, fg='black',  master=self.coneframe).grid(row=4, column=1, padx=5, pady=5)

        self.cl_generatrix = tk.Label(text="Generatrix: ",  height=3, fg='black',  master=self.coneframe).grid(row=5, column=0, padx=5, pady=5)
        self.ge = tk.StringVar()
        self.cl_gen = tk.Label(textvariable=self.ge,  height=3, fg='black',  master=self.coneframe).grid(row=5, column=1, padx=5, pady=5)

        self.cl_area = tk.Label(text="Area: ",  height=3, fg='black',  master=self.coneframe).grid(row=6, column=0, padx=5, pady=5)
        self.ar = tk.StringVar()
        self.cl_are = tk.Label(textvariable=self.ar,  height=3, fg='black',  master=self.coneframe).grid(row=6, column=1, padx=5, pady=5)
        self.cl_area_lateral = tk.Label(text="Lateral area: ",  height=3, fg='black',  master=self.coneframe).grid(row=7, column=0, padx=5, pady=5)
        self.lar = tk.StringVar()
        self.cl_lare = tk.Label(textvariable=self.lar,  height=3, fg='black',  master=self.coneframe).grid(row=7, column=1, padx=5, pady=5)
        self.cl_length = tk.Label(text="Volume: ",  height=3, fg='black',  master=self.coneframe).grid(row=8, column=0, padx=5, pady=5)
        self.le = tk.StringVar()
        self.cl_len = tk.Label(textvariable=self.le,  height=3, fg='black',  master=self.coneframe).grid(row=8, column=1, padx=5, pady=5)

    def calculus(self):
        try:
            cn = volume.Cone(int(self.re.get()), int(self.h.get()))
            self.rad.set(cn.radius)
            self.ar.set(cn.area())
            self.le.set(cn.volume())
            self.he.set(cn.height)
            self.ge.set(cn.generatrix)
            self.lar.set(cn.lateral_area())
        except ValueError:
            pass


class TkCylinder(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.cylinderframe = tk.Frame(self)
        self.circlelable = tk.Label(text="Enter radius",  height=3, fg='black',  master=self.cylinderframe).grid(row=0, column=0, padx=5, pady=5)
        self.circleresults = tk.Label(text="Results",  height=3, master=self.cylinderframe).grid(row=2, column=1, padx=5, pady=5)
        self.re = tk.StringVar()
        self.circleentry = tk.Entry(master=self.cylinderframe, width=10, textvariable=self.re).grid(row=0, column=1, padx=5, pady=5)
        self.circlebutton = tk.Button(master=self.cylinderframe, text='Ok', width=10, height=3, command=self.calculus).grid(row=0, column=2, padx=5, pady=5)
        self.circlelable = tk.Label(text="Enter hieght",  height=3, fg='black',  master=self.cylinderframe).grid(row=1, column=0, padx=5, pady=5)
        self.h = tk.StringVar()
        self.circleentry = tk.Entry(master=self.cylinderframe, width=10, textvariable=self.h).grid(row=1, column=1, padx=5, pady=5)
        self.cylinderframe.pack()

        self.cl_radius = tk.Label(text="Radius: ",  height=3, fg='black',  master=self.cylinderframe).grid(row=3, column=0, padx=5, pady=5)
        self.rad = tk.StringVar()
        self.cl_rad = tk.Label(textvariable=self.rad,  height=3, fg='black',  master=self.cylinderframe).grid(row=3, column=1, padx=5, pady=5)
        self.cl_height = tk.Label(text="Height: ",  height=3, fg='black',  master=self.cylinderframe).grid(row=4, column=0, padx=5, pady=5)
        self.he = tk.StringVar()
        self.cl_hgt = tk.Label(textvariable=self.he,  height=3, fg='black',  master=self.cylinderframe).grid(row=4, column=1, padx=5, pady=5)
        self.cl_area = tk.Label(text="Area: ",  height=3, fg='black',  master=self.cylinderframe).grid(row=5, column=0, padx=5, pady=5)
        self.ar = tk.StringVar()
        self.cl_are = tk.Label(textvariable=self.ar,  height=3, fg='black',  master=self.cylinderframe).grid(row=5, column=1, padx=5, pady=5)
        self.cl_area_base = tk.Label(text="Base area: ",  height=3, fg='black',  master=self.cylinderframe).grid(row=6, column=0, padx=5, pady=5)
        self.bar = tk.StringVar()
        self.cl_bare = tk.Label(textvariable=self.bar,  height=3, fg='black',  master=self.cylinderframe).grid(row=6, column=1, padx=5, pady=5)
        self.cl_area_lateral = tk.Label(text="Lateral area: ",  height=3, fg='black',  master=self.cylinderframe).grid(row=7, column=0, padx=5, pady=5)
        self.lar = tk.StringVar()
        self.cl_lare = tk.Label(textvariable=self.lar,  height=3, fg='black',  master=self.cylinderframe).grid(row=7, column=1, padx=5, pady=5)
        self.cl_length = tk.Label(text="Volume: ",  height=3, fg='black',  master=self.cylinderframe).grid(row=8, column=0, padx=5, pady=5)
        self.le = tk.StringVar()
        self.cl_len = tk.Label(textvariable=self.le,  height=3, fg='black',  master=self.cylinderframe).grid(row=8, column=1, padx=5, pady=5)

    def calculus(self):
        try:
            clr = volume.Cylinder(int(self.re.get()), int(self.h.get()))
            self.rad.set(clr.radius)
            self.ar.set(clr.area())
            self.le.set(clr.volume())
            self.he.set(clr.height)
            self.bar.set(clr.top_area())
            self.lar.set(clr.lateral_area())
        except ValueError:
            pass


class TkParallelepiped(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parallelepipedframe = tk.Frame(self)
        self.triangleresults = tk.Label(text="Results",  height=3, master=self.parallelepipedframe).grid(row=3, column=1, padx=5, pady=5)
        self.trianglebutton = tk.Button(master=self.parallelepipedframe, text='Ok', width=10, height=3, command=self.calculus).grid(row=0, column=2, padx=5, pady=5)

        self.a = tk.StringVar()
        self.trianglelable_a = tk.Label(text="Enter siade a",  height=3, fg='black',  master=self.parallelepipedframe).grid(row=0, column=0, padx=5, pady=5)
        self.triangleentry_a = tk.Entry(master=self.parallelepipedframe, width=10, textvariable=self.a).grid(row=0, column=1, padx=5, pady=5)

        self.b = tk.StringVar()
        self.trianglelable_b = tk.Label(text="Enter side b",  height=3, fg='black',  master=self.parallelepipedframe).grid(row=1, column=0, padx=5, pady=5)
        self.triangleentry_b = tk.Entry(master=self.parallelepipedframe, width=10, textvariable=self.b).grid(row=1, column=1, padx=5, pady=5)

        self.c = tk.StringVar()
        self.trianglelable_c = tk.Label(text="Enter side c",  height=3, fg='black',  master=self.parallelepipedframe).grid(row=2, column=0, padx=5, pady=5)
        self.triangleentry_c = tk.Entry(master=self.parallelepipedframe, width=10, textvariable=self.c).grid(row=2, column=1, padx=5, pady=5)

        self.parallelepipedframe.pack()

        self.si_a = tk.Label(text="Side a: ",  height=3, fg='black',  master=self.parallelepipedframe).grid(row=4, column=0, padx=5, pady=5)
        self.sa = tk.StringVar()
        self.r_sa = tk.Label(textvariable=self.sa,  height=3, fg='black',  master=self.parallelepipedframe).grid(row=4, column=1, padx=5, pady=5)
        self.si_b = tk.Label(text="Side b: ",  height=3, fg='black',  master=self.parallelepipedframe).grid(row=5, column=0, padx=5, pady=5)
        self.sb = tk.StringVar()
        self.r_sb = tk.Label(textvariable=self.sb,  height=3, fg='black',  master=self.parallelepipedframe).grid(row=5, column=1, padx=5, pady=5)
        self.si_c = tk.Label(text="Side c: ",  height=3, fg='black',  master=self.parallelepipedframe).grid(row=6, column=0, padx=5, pady=5)
        self.sc = tk.StringVar()
        self.r_sc = tk.Label(textvariable=self.sc,  height=3, fg='black',  master=self.parallelepipedframe).grid(row=6, column=1, padx=5, pady=5)

        self.si_diagonal = tk.Label(text="Diagonel: ",  height=3, fg='black',  master=self.parallelepipedframe).grid(row=7, column=0, padx=5, pady=5)
        self.dg = tk.StringVar()
        self.r_dig = tk.Label(textvariable=self.dg,  height=3, fg='black',  master=self.parallelepipedframe).grid(row=7, column=1, padx=5, pady=5)

        self.si_area = tk.Label(text="Area: ",  height=3, fg='black',  master=self.parallelepipedframe).grid(row=8, column=0, padx=5, pady=5)
        self.ar = tk.StringVar()
        self.r_ar = tk.Label(textvariable=self.ar,  height=3, fg='black',  master=self.parallelepipedframe).grid(row=8, column=1, padx=5, pady=5)

        self.si_volume = tk.Label(text="Volume: ",  height=3, fg='black',  master=self.parallelepipedframe).grid(row=9, column=0, padx=5, pady=5)
        self.vl = tk.StringVar()
        self.r_vol = tk.Label(textvariable=self.vl,  height=3, fg='black',  master=self.parallelepipedframe).grid(row=9, column=1, padx=5, pady=5)

    def calculus(self):
        try:
            ppd = volume.Parallelepiped(int(self.a.get()), int(self.b.get()), int(self.c.get()))
            self.sa.set(ppd.a)
            self.sb.set(ppd.b)
            self.sc.set(ppd.c)
            self.dg.set(ppd.diagonal())
            self.ar.set(ppd.area())
            self.vl.set(ppd.volume())
        except ValueError:
            pass


class TkSphere(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.sphereframe = tk.Frame(self)
        self.circlelable = tk.Label(text="Enter radius of sphere",  height=3, fg='black',  master=self.sphereframe).grid(row=0, column=0, padx=5, pady=5)
        self.circleresults = tk.Label(text="Results",  height=3, master=self.sphereframe).grid(row=1, column=1, padx=5, pady=5)
        self.re = tk.StringVar()
        self.circleentry = tk.Entry(master=self.sphereframe, width=10, textvariable=self.re).grid(row=0, column=1, padx=5, pady=5)
        self.circlebutton = tk.Button(master=self.sphereframe, text='Ok', width=10, height=3, command=self.calculus).grid(row=0, column=2, padx=5, pady=5)
        self.sphereframe.pack()

        self.cl_radius = tk.Label(text="Radius: ",  height=3, fg='black',  master=self.sphereframe).grid(row=2, column=0, padx=5, pady=5)
        self.rad = tk.StringVar()
        self.cl_rad = tk.Label(textvariable=self.rad,  height=3, fg='black',  master=self.sphereframe).grid(row=2, column=1, padx=5, pady=5)
        self.cl_area = tk.Label(text="Area: ",  height=3, fg='black',  master=self.sphereframe).grid(row=3, column=0, padx=5, pady=5)
        self.ar = tk.StringVar()
        self.cl_are = tk.Label(textvariable=self.ar,  height=3, fg='black',  master=self.sphereframe).grid(row=3, column=1, padx=5, pady=5)
        self.cl_length = tk.Label(text="Volume: ",  height=3, fg='black',  master=self.sphereframe).grid(row=4, column=0, padx=5, pady=5)
        self.le = tk.StringVar()
        self.cl_len = tk.Label(textvariable=self.le,  height=3, fg='black',  master=self.sphereframe).grid(row=4, column=1, padx=5, pady=5)

    def calculus(self):
        try:
            spr = volume.Sphere(int(self.re.get()))
            self.rad.set(spr.radius)
            self.ar.set(spr.area())
            self.le.set(spr.volume())
        except ValueError:
            pass


class TkCube(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.cubeframe = tk.Frame(self)
        self.sqarelable = tk.Label(text="Enter side of square",  height=3, fg='black',  master=self.cubeframe).grid(row=0, column=0, padx=5, pady=5)
        self.sqareeresults = tk.Label(text="Results",  height=3, master=self.cubeframe).grid(row=1, column=1, padx=5, pady=5)
        self.re = tk.StringVar()
        self.sqareentry = tk.Entry(master=self.cubeframe, width=10, textvariable=self.re).grid(row=0, column=1, padx=5, pady=5)
        self.sqarebutton = tk.Button(master=self.cubeframe, text='Ok', width=10, height=3, command=self.calculus).grid(row=0, column=2, padx=5, pady=5)
        self.cubeframe.pack()

        self.sq_side = tk.Label(text="Side: ",  height=3, fg='black',  master=self.cubeframe).grid(row=2, column=0, padx=5, pady=5)
        self.sid = tk.StringVar()
        self.sq_sid = tk.Label(textvariable=self.sid,  height=3, fg='black',  master=self.cubeframe).grid(row=2, column=1, padx=5, pady=5)
        self.sq_area = tk.Label(text="Area: ",  height=3, fg='black',  master=self.cubeframe).grid(row=3, column=0, padx=5, pady=5)
        self.ar = tk.StringVar()
        self.sq_are = tk.Label(textvariable=self.ar,  height=3, fg='black',  master=self.cubeframe).grid(row=3, column=1, padx=5, pady=5)
        self.sq_length = tk.Label(text="Perimiter: ",  height=3, fg='black',  master=self.cubeframe).grid(row=4, column=0, padx=5, pady=5)
        self.le = tk.StringVar()
        self.sq_len = tk.Label(textvariable=self.le,  height=3, fg='black',  master=self.cubeframe).grid(row=4, column=1, padx=5, pady=5)
        self.sq_volume = tk.Label(text="Volume: ",  height=3, fg='black',  master=self.cubeframe).grid(row=5, column=0, padx=5, pady=5)
        self.vl = tk.StringVar()
        self.sq_vol = tk.Label(textvariable=self.vl,  height=3, fg='black',  master=self.cubeframe).grid(row=5, column=1, padx=5, pady=5)

    def calculus(self):
        try:
            cb = volume.Cube(int(self.re.get()))
            self.sid.set(cb.side)
            self.ar.set(cb.area())
            self.le.set(cb.perimeter())
            self.vl.set(cb.volume())
        except ValueError:
            pass


class FlatF(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        figures = {'Circle': self.circle_calc, 'Square': self.square_calc, 'Triangle': self.triangle_calc, \
                    'Rectangle': self.rectangle_calc, 'Rhombus': self.rhombus_calc, 'Trapezoid': self.trapezoid_calc}
        self.title("Плоские фигуры")
        self.flatframe = tk.Frame(self)
        r = 0
        c = 0
        k = 0
        for i, j in figures.items():
            if k % 3 == 0 and k != 0:
                c = 0
                r += 1
            tk.Button(text=i, width=30, height=10, bg='grey', fg='black', master=self.flatframe, command=j).grid(row=r, column=c)
            c += 1
            k += 1
        self.flatframe.pack()

    def circle_calc(self) -> None:
        tc = TkCircle(self)
        tc.grab_set()

    def square_calc(self) -> None:
        sc = TkSquare(self)
        sc.grab_set()

    def triangle_calc(self) -> None:
        ti = TkTriangle(self)
        ti.grab_set()

    def rectangle_calc(self) -> None:
        rc = TkRectangle(self)
        rc.grab_set()

    def rhombus_calc(self) -> None:
        rb = TkRhombus(self)
        rb.grab_set()

    def trapezoid_calc(self) -> None:
        tp = TkTrapezoid(self)
        tp.grab_set()


class TkCircle(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.circleframe = tk.Frame(self)
        self.circlelable = tk.Label(text="Enter radius of circle", height=3, fg='black',  master=self.circleframe).grid(row=0, column=0, padx=5, pady=5)
        self.circleresults = tk.Label(text="Results",  height=3, master=self.circleframe).grid(row=1, column=1, padx=5, pady=5)
        self.re = tk.StringVar()
        self.circleentry = tk.Entry(master=self.circleframe, width=10, textvariable=self.re).grid(row=0, column=1, padx=5, pady=5)
        self.circlebutton = tk.Button(master=self.circleframe, text='Ok', width=10, height=3, command=self.calculus).grid(row=0, column=2, padx=5, pady=5)
        self.circleframe.pack()

        self.cl_radius = tk.Label(text="Radius: ",  height=3, fg='black',  master=self.circleframe).grid(row=2, column=0, padx=5, pady=5)
        self.rad = tk.StringVar()
        self.cl_rad = tk.Label(textvariable=self.rad,  height=3, fg='black',  master=self.circleframe).grid(row=2, column=1, padx=5, pady=5)
        self.cl_diameter = tk.Label(text="Diameter: ",  height=3, fg='black',  master=self.circleframe).grid(row=3, column=0, padx=5, pady=5)
        self.dia = tk.StringVar()
        self.cl_dia = tk.Label(textvariable=self.dia,  height=3, fg='black',  master=self.circleframe).grid(row=3, column=1, padx=5, pady=5)
        self.cl_area = tk.Label(text="Area: ",  height=3, fg='black',  master=self.circleframe).grid(row=4, column=0, padx=5, pady=5)
        self.ar = tk.StringVar()
        self.cl_are = tk.Label(textvariable=self.ar,  height=3, fg='black',  master=self.circleframe).grid(row=4, column=1, padx=5, pady=5)
        self.cl_length = tk.Label(text="Length: ",  height=3, fg='black',  master=self.circleframe).grid(row=5, column=0, padx=5, pady=5)
        self.le = tk.StringVar()
        self.cl_len = tk.Label(textvariable=self.le,  height=3, fg='black',  master=self.circleframe).grid(row=5, column=1, padx=5, pady=5)

    def calculus(self):
        try:
            crc = flat.Circle(int(self.re.get()))
            self.rad.set(crc.radius)
            self.dia.set(crc.diameter)
            self.ar.set(crc.area())
            self.le.set(crc.perimeter())
        except ValueError:
            pass


class TkSquare(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.squareframe = tk.Frame(self)
        self.sqarelable = tk.Label(text="Enter side of square",  height=3, fg='black',  master=self.squareframe).grid(row=0, column=0, padx=5, pady=5)
        self.sqareeresults = tk.Label(text="Results",  height=3, master=self.squareframe).grid(row=1, column=1, padx=5, pady=5)
        self.re = tk.StringVar()
        self.sqareentry = tk.Entry(master=self.squareframe, width=10, textvariable=self.re).grid(row=0, column=1, padx=5, pady=5)
        self.sqarebutton = tk.Button(master=self.squareframe, text='Ok', width=10, height=3, command=self.calculus).grid(row=0, column=2, padx=5, pady=5)
        self.squareframe.pack()

        self.sq_side = tk.Label(text="Side: ",  height=3, fg='black',  master=self.squareframe).grid(row=2, column=0, padx=5, pady=5)
        self.sid = tk.StringVar()
        self.sq_sid = tk.Label(textvariable=self.sid,  height=3, fg='black',  master=self.squareframe).grid(row=2, column=1, padx=5, pady=5)
        self.sq_area = tk.Label(text="Area: ",  height=3, fg='black',  master=self.squareframe).grid(row=3, column=0, padx=5, pady=5)
        self.ar = tk.StringVar()
        self.sq_are = tk.Label(textvariable=self.ar,  height=3, fg='black',  master=self.squareframe).grid(row=3, column=1, padx=5, pady=5)
        self.sq_length = tk.Label(text="Perimiter: ",  height=3, fg='black',  master=self.squareframe).grid(row=4, column=0, padx=5, pady=5)
        self.le = tk.StringVar()
        self.sq_len = tk.Label(textvariable=self.le,  height=3, fg='black',  master=self.squareframe).grid(row=4, column=1, padx=5, pady=5)

    def calculus(self):
        try:
            sqr = flat.Sqare(int(self.re.get()))
            self.sid.set(sqr.side)
            self.ar.set(sqr.area())
            self.le.set(sqr.perimeter())
        except ValueError:
            pass


class TkTriangle(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.triangleframe = tk.Frame(self)
        self.triangleresults = tk.Label(text="Results",  height=3, master=self.triangleframe).grid(row=3, column=1, padx=5, pady=5)
        self.trianglebutton = tk.Button(master=self.triangleframe, text='Ok', width=10, height=3, command=self.calculus).grid(row=0, column=2, padx=5, pady=5)

        self.a = tk.StringVar()
        self.trianglelable_a = tk.Label(text="Enter siade a",  height=3, fg='black',  master=self.triangleframe).grid(row=0, column=0, padx=5, pady=5)
        self.triangleentry_a = tk.Entry(master=self.triangleframe, width=10, textvariable=self.a).grid(row=0, column=1, padx=5, pady=5)

        self.b = tk.StringVar()
        self.trianglelable_b = tk.Label(text="Enter side b",  height=3, fg='black',  master=self.triangleframe).grid(row=1, column=0, padx=5, pady=5)
        self.triangleentry_b = tk.Entry(master=self.triangleframe, width=10, textvariable=self.b).grid(row=1, column=1, padx=5, pady=5)

        self.c = tk.StringVar()
        self.trianglelable_c = tk.Label(text="Enter side c",  height=3, fg='black',  master=self.triangleframe).grid(row=2, column=0, padx=5, pady=5)
        self.triangleentry_c = tk.Entry(master=self.triangleframe, width=10, textvariable=self.c).grid(row=2, column=1, padx=5, pady=5)

        self.triangleframe.pack()

        self.si_a = tk.Label(text="Side a: ",  height=3, fg='black',  master=self.triangleframe).grid(row=4, column=0, padx=5, pady=5)
        self.sa = tk.StringVar()
        self.r_sa = tk.Label(textvariable=self.sa,  height=3, fg='black',  master=self.triangleframe).grid(row=4, column=1, padx=5, pady=5)
        self.si_b = tk.Label(text="Side b: ",  height=3, fg='black',  master=self.triangleframe).grid(row=5, column=0, padx=5, pady=5)
        self.sb = tk.StringVar()
        self.r_sb = tk.Label(textvariable=self.sb,  height=3, fg='black',  master=self.triangleframe).grid(row=5, column=1, padx=5, pady=5)
        self.si_c = tk.Label(text="Side c: ",  height=3, fg='black',  master=self.triangleframe).grid(row=6, column=0, padx=5, pady=5)
        self.sc = tk.StringVar()
        self.r_sc = tk.Label(textvariable=self.sc,  height=3, fg='black',  master=self.triangleframe).grid(row=6, column=1, padx=5, pady=5)

        self.si_perimiter = tk.Label(text="Perimiter: ",  height=3, fg='black',  master=self.triangleframe).grid(row=7, column=0, padx=5, pady=5)
        self.per = tk.StringVar()
        self.r_per = tk.Label(textvariable=self.per,  height=3, fg='black',  master=self.triangleframe).grid(row=7, column=1, padx=5, pady=5)

        self.si_area = tk.Label(text="Area: ",  height=3, fg='black',  master=self.triangleframe).grid(row=8, column=0, padx=5, pady=5)
        self.ar = tk.StringVar()
        self.r_ar = tk.Label(textvariable=self.ar,  height=3, fg='black',  master=self.triangleframe).grid(row=8, column=1, padx=5, pady=5)

    def calculus(self):
        try:
            tri = flat.Triangle(int(self.a.get()), int(self.b.get()), int(self.c.get()))
            self.sa.set(tri.a)
            self.sb.set(tri.b)
            self.sc.set(tri.c)
            self.per.set(tri.perimeter())
            self.ar.set(tri.area())
        except ValueError:
            pass


class TkRectangle(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.rectangleframe = tk.Frame(self)
        self.rectangleresults = tk.Label(text="Results",  height=3, master=self.rectangleframe).grid(row=2, column=1, padx=5, pady=5)
        self.rectanglebutton = tk.Button(master=self.rectangleframe, text='Ok', width=10, height=3, command=self.calculus).grid(row=0, column=2, padx=5, pady=5)

        self.a = tk.StringVar()
        self.rectanglelable_a = tk.Label(text="Enter siade a",  height=3, fg='black',  master=self.rectangleframe).grid(row=0, column=0, padx=5, pady=5)
        self.rectangleentry_a = tk.Entry(master=self.rectangleframe, width=10, textvariable=self.a).grid(row=0, column=1, padx=5, pady=5)

        self.b = tk.StringVar()
        self.rectanglelable_b = tk.Label(text="Enter side b",  height=3, fg='black',  master=self.rectangleframe).grid(row=1, column=0, padx=5, pady=5)
        self.rectangleentry_b = tk.Entry(master=self.rectangleframe, width=10, textvariable=self.b).grid(row=1, column=1, padx=5, pady=5)

        self.rectangleframe.pack()

        self.si_a = tk.Label(text="Side a: ",  height=3, fg='black',  master=self.rectangleframe).grid(row=3, column=0, padx=5, pady=5)
        self.sa = tk.StringVar()
        self.r_sa = tk.Label(textvariable=self.sa,  height=3, fg='black',  master=self.rectangleframe).grid(row=3, column=1, padx=5, pady=5)
        self.si_b = tk.Label(text="Side b: ",  height=3, fg='black',  master=self.rectangleframe).grid(row=4, column=0, padx=5, pady=5)
        self.sb = tk.StringVar()
        self.r_sb = tk.Label(textvariable=self.sb,  height=3, fg='black',  master=self.rectangleframe).grid(row=4, column=1, padx=5, pady=5)

        self.si_perimiter = tk.Label(text="Perimiter: ",  height=3, fg='black',  master=self.rectangleframe).grid(row=5, column=0, padx=5, pady=5)
        self.per = tk.StringVar()
        self.r_per = tk.Label(textvariable=self.per,  height=3, fg='black',  master=self.rectangleframe).grid(row=5, column=1, padx=5, pady=5)

        self.si_area = tk.Label(text="Area: ",  height=3, fg='black',  master=self.rectangleframe).grid(row=6, column=0, padx=5, pady=5)
        self.ar = tk.StringVar()
        self.r_ar = tk.Label(textvariable=self.ar,  height=3, fg='black',  master=self.rectangleframe).grid(row=6, column=1, padx=5, pady=5)

    def calculus(self):
        try:
            rect = flat.Rectangle(int(self.a.get()), int(self.b.get()))
            self.sa.set(rect.a)
            self.sb.set(rect.b)
            self.per.set(rect.perimeter())
            self.ar.set(rect.area())
        except ValueError:
            pass


class TkRhombus(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.rhombusframe = tk.Frame(self)
        self.rectangleresults = tk.Label(text="Results",  height=3, master=self.rhombusframe).grid(row=2, column=1, padx=5, pady=5)
        self.rectanglebutton = tk.Button(master=self.rhombusframe, text='Ok', width=10, height=3, command=self.calculus).grid(row=0, column=2, padx=5, pady=5)

        self.a = tk.StringVar()
        self.rectanglelable_a = tk.Label(text="Enter diagonal big",  height=3, fg='black',  master=self.rhombusframe).grid(row=0, column=0, padx=5, pady=5)
        self.rectangleentry_a = tk.Entry(master=self.rhombusframe, width=10, textvariable=self.a).grid(row=0, column=1, padx=5, pady=5)

        self.b = tk.StringVar()
        self.rectanglelable_b = tk.Label(text="Enter diagonal small",  height=3, fg='black',  master=self.rhombusframe).grid(row=1, column=0, padx=5, pady=5)
        self.rectangleentry_b = tk.Entry(master=self.rhombusframe, width=10, textvariable=self.b).grid(row=1, column=1, padx=5, pady=5)

        self.rhombusframe .pack()

        self.si_a = tk.Label(text="Diagonal big: ",  height=3, fg='black',  master=self.rhombusframe).grid(row=3, column=0, padx=5, pady=5)
        self.sa = tk.StringVar()
        self.r_sa = tk.Label(textvariable=self.sa,  height=3, fg='black',  master=self.rhombusframe).grid(row=3, column=1, padx=5, pady=5)
        self.si_b = tk.Label(text="Diagonal small: ",  height=3, fg='black',  master=self.rhombusframe).grid(row=4, column=0, padx=5, pady=5)
        self.sb = tk.StringVar()
        self.r_sb = tk.Label(textvariable=self.sb,  height=3, fg='black',  master=self.rhombusframe).grid(row=4, column=1, padx=5, pady=5)
        self.si_c = tk.Label(text="Side: ",  height=3, fg='black',  master=self.rhombusframe).grid(row=5, column=0, padx=5, pady=5)
        self.sc = tk.StringVar()
        self.r_sc = tk.Label(textvariable=self.sb,  height=3, fg='black',  master=self.rhombusframe).grid(row=5, column=1, padx=5, pady=5)

        self.si_perimiter = tk.Label(text="Perimiter: ",  height=3, fg='black',  master=self.rhombusframe).grid(row=6, column=0, padx=5, pady=5)
        self.per = tk.StringVar()
        self.r_per = tk.Label(textvariable=self.per,  height=3, fg='black',  master=self.rhombusframe).grid(row=6, column=1, padx=5, pady=5)

        self.si_area = tk.Label(text="Area: ",  height=3, fg='black',  master=self.rhombusframe).grid(row=7, column=0, padx=5, pady=5)
        self.ar = tk.StringVar()
        self.r_ar = tk.Label(textvariable=self.ar,  height=3, fg='black',  master=self.rhombusframe).grid(row=7, column=1, padx=5, pady=5)

    def calculus(self):
        try:
            rmb = flat.Rhombus(int(self.a.get()), int(self.b.get()))
            self.sa.set(rmb.big_diagonal)
            self.sb.set(rmb.short_diagonal)
            self.per.set(rmb.perimeter())
            self.ar.set(rmb.area())
        except ValueError:
            pass


class TkTrapezoid(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.trapezoidframe = tk.Frame(self)
        self.triangleresults = tk.Label(text="Results",  height=3, master=self.trapezoidframe).grid(row=4, column=1, padx=5, pady=5)
        self.trianglebutton = tk.Button(master=self.trapezoidframe, text='Ok', width=10, height=3, command=self.calculus).grid(row=0, column=2, padx=5, pady=5)

        self.a = tk.StringVar()
        self.trianglelable_a = tk.Label(text="Enter siade a",  height=3, fg='black',  master=self.trapezoidframe).grid(row=0, column=0, padx=5, pady=5)
        self.triangleentry_a = tk.Entry(master=self.trapezoidframe, width=10, textvariable=self.a).grid(row=0, column=1, padx=5, pady=5)

        self.b = tk.StringVar()
        self.trianglelable_b = tk.Label(text="Enter side b",  height=3, fg='black',  master=self.trapezoidframe).grid(row=1, column=0, padx=5, pady=5)
        self.triangleentry_b = tk.Entry(master=self.trapezoidframe, width=10, textvariable=self.b).grid(row=1, column=1, padx=5, pady=5)

        self.c = tk.StringVar()
        self.trianglelable_c = tk.Label(text="Enter side c",  height=3, fg='black',  master=self.trapezoidframe).grid(row=2, column=0, padx=5, pady=5)
        self.triangleentry_c = tk.Entry(master=self.trapezoidframe, width=10, textvariable=self.c).grid(row=2, column=1, padx=5, pady=5)

        self.d = tk.StringVar()
        self.trianglelable_d = tk.Label(text="Enter side d",  height=3, fg='black',  master=self.trapezoidframe).grid(row=3, column=0, padx=5, pady=5)
        self.triangleentry_d = tk.Entry(master=self.trapezoidframe, width=10, textvariable=self.d).grid(row=3, column=1, padx=5, pady=5)

        self.trapezoidframe.pack()

        self.si_a = tk.Label(text="Side a: ",  height=3, fg='black',  master=self.trapezoidframe).grid(row=5, column=0, padx=5, pady=5)
        self.sa = tk.StringVar()
        self.r_sa = tk.Label(textvariable=self.sa,  height=3, fg='black',  master=self.trapezoidframe).grid(row=5, column=1, padx=5, pady=5)
        self.si_b = tk.Label(text="Side b: ",  height=3, fg='black',  master=self.trapezoidframe).grid(row=6, column=0, padx=5, pady=5)
        self.sb = tk.StringVar()
        self.r_sb = tk.Label(textvariable=self.sb,  height=3, fg='black',  master=self.trapezoidframe).grid(row=6, column=1, padx=5, pady=5)
        self.si_c = tk.Label(text="Side c: ",  height=3, fg='black',  master=self.trapezoidframe).grid(row=7, column=0, padx=5, pady=5)
        self.sc = tk.StringVar()
        self.r_sc = tk.Label(textvariable=self.sc,  height=3, fg='black',  master=self.trapezoidframe).grid(row=7, column=1, padx=5, pady=5)
        self.si_d = tk.Label(text="Side c: ",  height=3, fg='black',  master=self.trapezoidframe).grid(row=8, column=0, padx=5, pady=5)
        self.sd = tk.StringVar()
        self.r_sd = tk.Label(textvariable=self.sd,  height=3, fg='black',  master=self.trapezoidframe).grid(row=8, column=1, padx=5, pady=5)

        self.si_perimiter = tk.Label(text="Perimiter: ",  height=3, fg='black',  master=self.trapezoidframe).grid(row=9, column=0, padx=5, pady=5)
        self.per = tk.StringVar()
        self.r_per = tk.Label(textvariable=self.per,  height=3, fg='black',  master=self.trapezoidframe).grid(row=9, column=1, padx=5, pady=5)

        self.si_area = tk.Label(text="Area: ",  height=3, fg='black',  master=self.trapezoidframe).grid(row=10, column=0, padx=5, pady=5)
        self.ar = tk.StringVar()
        self.r_ar = tk.Label(textvariable=self.ar,  height=3, fg='black',  master=self.trapezoidframe).grid(row=10, column=1, padx=5, pady=5)

    def calculus(self):
        try:
            trp = flat.Trapezoid(int(self.a.get()), int(self.b.get()), int(self.c.get()), int(self.d.get()))
            self.sa.set(trp.a)
            self.sb.set(trp.b)
            self.sc.set(trp.c)
            self.sd.set(trp.d)
            self.per.set(trp.perimeter())
            self.ar.set(trp.area())
        except ValueError:
            pass


class Calculator(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.geometry('600x200+{}+{}'.format((self.winfo_screenmmwidth() + 300) // 2, (self.winfo_screenheight() - 100) // 2))
        self.title("Геометрический калькулятор")
        self.frame = tk.Frame()
        self.btn_volume = tk.Button(text='Volume figures.', width=30, height=15, \
                            bg='grey', fg='black', master=self.frame, \
                                command=self.volume_figures).grid(row=0, column=0, padx=10, pady=5)
        self.btn_flat = tk.Button(text='Flat figures.', width=30, height=15, \
                            bg='grey', fg='black', master=self.frame, \
                                command=self.flat_figures).grid(row=0, column=1, padx=10, pady=5)
        self.frame.pack()

    def volume_figures(self):
        volume = VolumeF(self)
        volume.grab_set()

    def flat_figures(self):
        flat = FlatF(self)
        flat.grab_set()


def main():
    app = Calculator()
    app.mainloop()


if __name__ == '__main__':
    main()
