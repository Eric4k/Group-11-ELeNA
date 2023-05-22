import L from "leaflet";
import { useMap } from "react-leaflet";


export default function Route(props) {
  const map = useMap();

  map.eachLayer(layer => map.removeLayer(layer));

  L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    }).addTo(map);

  if (props.coord.length !== 0) {

    props.coord.forEach((coord, index) => {
      if (index === 0) {
        L.marker(coord).addTo(map).bindPopup(props.source);
      }
      if (index === props.coord.length - 1) {
        L.marker(coord).addTo(map).bindPopup(props.dest);
      }
    });

    let line = L.polyline(props.coord).addTo(map);

    map.fitBounds(line.getBounds());
    }
  return null;
}
