import L from "leaflet";
import { useMap } from "react-leaflet";


export default function Route(props) {
  const map = useMap();

  map.eachLayer(layer => map.removeLayer(layer));

  props.coord.forEach((coord, index) => {
    if (index === 0 || index === props.coord.length - 1) {
      L.marker(coord).addTo(map);
    }
  });

  let line = L.polyline(props.coord).addTo(map);

  L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution:
      '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
  }).addTo(map);

  map.fitBounds(line.getBounds());

  return null;
}
