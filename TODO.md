# TODO - Nearest road distance route deviation

- [x] Add `getNearestRoadDistance(lat, lng)` to `dashboard.html` using existing loaded `roadsGeoJSON`.
- [x] Ensure roads data is accessible to the function (use `roadsGeoJSON` or `window.roadsGeoJSON`).
- [x] Decide threshold constant (meters) for route deviation, and apply it.
- [x] Update UI: show nearest road distance in the info box.
- [x] Update route status logic to: buffer check OR nearest-distance-threshold => inside approved route, else deviation.

- [ ] Test in browser: reload dashboard and verify status changes when moving off-route.

