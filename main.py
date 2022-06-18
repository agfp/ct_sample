import cameratransform as ct
import json
from PIL import Image
import geojsonreader
import helpers

### Variables for Biospatial_20210705_PORT_1097.JPG

image_path       = 'data/Biospatial_20210705_PORT_1097.JPG'
geojson_path     = 'data/Ellipsoid_MangrovePolygon.geojson'
#geojson_path     = 'data/Ellipsoid_MangroveBoundingBox.geojson'
camera_latitude  = -36.46268
camera_longitude = 174.701975
camera_altitude  = 360.912796
yaw              = 77.773732
pitch            = 68.539041
roll             = 1.110635
focal_length_mm  = 25.0
sensor_size_w_mm = 35.9
sensor_size_h_mm = 24.0
distortion_k1    = None
distortion_k2    = None
distortion_k3    = None

### Variables for Biospatial_20210705_PORT_1230.JPG

# image_path       = 'data/Biospatial_20210705_PORT_1230.JPG'
# geojson_path     = 'data/Ellipsoid_MangrovePolygon.geojson'
# #geojson_path     = 'data/Ellipsoid_MangroveBoundingBox.geojson'
# camera_latitude  = -36.462231
# camera_longitude = 174.713123
# camera_altitude  = 335.937678
# yaw              = 267.839741
# pitch            = 68.441744
# roll             = 0.920125
# focal_length_mm  = 25.0
# sensor_size_w_mm = 35.9
# sensor_size_h_mm = 24.0
# distortion_k1    = None
# distortion_k2    = None
# distortion_k3    = None

### Pre-processing

img = Image.open(image_path)
image_width = img.width
image_height = img.height

f = open(geojson_path)
geojson = json.load(f)
coordinates = geojsonreader.parse(geojson)

### CameraTransform

projection = ct.RectilinearProjection(focallength_mm=focal_length_mm, 
    image_width_px=image_width, image_height_px=image_height, 
    sensor_width_mm=sensor_size_w_mm, sensor_height_mm=sensor_size_h_mm)

distortion = None
if (distortion_k1 is not None and distortion_k2 is not None and distortion_k3 is not None):
    distortion = ct.BrownLensDistortion(distortion_k1, distortion_k2, distortion_k3, projection)

orientation = ct.SpatialOrientation(heading_deg=yaw-90, tilt_deg=pitch, roll_deg=roll)
cam = ct.Camera(projection, orientation, distortion)
cam.setGPSpos(camera_longitude, camera_latitude, camera_altitude)

results = []
for c in coordinates:
    results.append(cam.imageFromGPS(c))

helpers.plot(image_path, results)

