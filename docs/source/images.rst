
******
Images
******

.. todo add examples

Images can be changed to work with bootstrap by add the `:class:` atrribute
to `.. image::` or `.. figure::` directives. Supported options are:

- `img-rounded`
- `img-circle`
- `img-thumbnail`
- `img-responsive`

Rounded Corners
===============

.. code:: rst

   .. figure:: https://www.w3schools.com/w3images/lights.jpg
      :class: img-rounded

.. figure:: https://www.w3schools.com/w3images/lights.jpg
   :class: img-rounded


Circle
======

.. code:: rst

   .. figure:: https://www.w3schools.com/w3images/lights.jpg
      :class: img-circle

.. figure:: https://www.w3schools.com/w3images/lights.jpg
   :class: img-circle


Thumbnails
==========

.. code:: rst

   .. figure:: https://www.w3schools.com/w3images/lights.jpg
      :class: img-thumbnail

.. figure:: https://www.w3schools.com/w3images/lights.jpg
   :class: img-thumbnail


Responsive Images
=================

.. note:: This will not work if you set the `:height:` or the `:width:` of the image.
  
.. code:: rst

   .. figure:: https://www.w3schools.com/w3images/lights.jpg
      :class: img-responsive

.. figure:: https://www.w3schools.com/w3images/lights.jpg
   :class: img-responsive
