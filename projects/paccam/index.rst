---
project: paccam
title: Paccam
short: A tool that assists users of laser cutters to make overlap-free 2D layouts.
long: A tool that assists users of laser cutters to make overlap-free 2D layouts.
picture: paccam.jpg
papers:
- saakes_uist_2013
team:
- Thomas Cambazard (EPFL),
- Jun Mitani (Tsukuba University) 
- Takeo Igarashi (University of Tokyo).
---
Many objects that we daily use such as furniture and clothing, start as
flat material on sheets or in rolls. Computer numerical control (CNC)
fabrication devices cut these materials into multiple 2D parts that make
up 3D objects.

.. vimeo:: 74930322åœ

The material inside a lasercutter is captured by an overlooking webcam
(a) mounted in the lid. By fabricating callibration patterns with the
laser cutter we establish the relationship between the camera image and
lasercutter coordinate system. Once calibrated, users simply take a
picture (b) with the attached buttons. We also report of a precise
method using the lasercutter preview laser as a scanner. A cheap
photodiode (c) measures the reflection (d) of the preview laser and so
the presence of material is related to a position x,y of the toolhead.

.. figure:: img/capture.png
    :alt: material capture methods

    We explored two methods to capture materials: fast
    with an overhead webcam (a) activated with a button (b) and precise with
    transforming the laser (c) into a scanning device (d). Simple background
    removal results in a vector representation of the edges of the materials (e-h).

The captured material functions as a constraint in the interactive user
interface to make an overlap free layout. The interface is based on
observation how people pack parts and based on earlier work in snapping
and physics on the desktop. In a 2D rigid body simulation, selected
parts collide, reorient and slide to other parts, but do not move other
parts. Several interactions are explored such as push to move parts,
compressing a selection, moving all parts to a side of the table.

.. figure:: img/packing.png
   :alt: Overlap Free packing

   Overlap Free packing