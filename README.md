surbar
=====

a collection of quickly written chunks of logic to identify pupil positions, draw censor bars, and then jam out to a video

the previous experiemnt [cenbar](https://github.com/phillipsm/cenbar) is closely related


### Helpful commands when playing with surbar

add bars to each image
`$python draw_on_images.py`

draw sticky bars on frames -- when a bar is drawn, it doesn't disappear, subsequent sticky bars are added
`$python draw_on_images_additive.py`

draw bars for each face - all on one image
`$python draw_one_image.py`


get xy coords for pupils for faces in an image
`$python get_numbers.py`


resize all images
`$convert ‘*.JPG[1200x]' resized%03d.png`


jpegs -> mpg
`$convert -delay 18 -compress None *.JPG movie.mpg`



## License

Dual licensed under the MIT license (below) and [GPL license](http://www.gnu.org/licenses/gpl-3.0.html).

<small>
MIT License

Copyright (c) 2016 Matt Phillips

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
</small>
