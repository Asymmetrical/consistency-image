All good questions, from the customer conversations i have been a part of, the picture i get is that the main issues are subject identity, product shape, and brand style, but generally of course everyone wants all of the above.

The problem at least in my eyes is that we have no solid way of measuring good/bad in a lot of cases, as style is entirely subjective and VLMs still struggle with the small details.

For over all style review we could get some of the way there if we provide 10 to 30 images of the same style to a vlm so it can understand the significant parts but still no promises of it being perfect.

I wonder however, @Pelle Johnsen Do you know of any consistent way to evaluate how good a mesh is?

Pelle on 3D models

Pelle Johnsen  [9:41 AM]
There are some metrics you can look at, but highly depends on usecase. Examples: polycount, quads vs. tris/ngons. These are all very technical and probably not what most users need. The more artistic are about topology and edgeflow, but I don't think there is any objective ways to measure this ... maybe again something very technical like amount of poles. Anyway in short to my knowledge there are no objective "metrics" for measuring the "artistic" quality of  a mesh.