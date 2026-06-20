const mapDataElement = document.getElementById("travel-map-data");
const mapElements = document.querySelectorAll("[data-travel-map]");

if (mapDataElement && mapElements.length && window.L) {
    const places = JSON.parse(mapDataElement.textContent);
    const coordinates = places.map((place) => place.coordinates);

    const markerIcon = L.divIcon({
        className: "travel-marker-wrapper",
        html: '<span class="travel-marker" aria-hidden="true"></span>',
        iconAnchor: [11, 25],
        iconSize: [22, 28],
        popupAnchor: [0, -24],
    });

    mapElements.forEach((element) => {
        const isPreview = element.dataset.mapMode === "preview";
        const fitMapToPlaces = () => {
            map.fitBounds(coordinates, {
                padding: isPreview ? [20, 20] : [44, 44],
                maxZoom: isPreview ? 1 : 3,
            });
        };
        const map = L.map(element, {
            attributionControl: !isPreview,
            dragging: !isPreview,
            keyboard: !isPreview,
            maxBounds: [[-85, -180], [85, 180]],
            maxBoundsViscosity: 1,
            scrollWheelZoom: false,
            touchZoom: !isPreview,
            doubleClickZoom: !isPreview,
            boxZoom: !isPreview,
            zoomControl: !isPreview,
            worldCopyJump: false,
            zoomSnap: 0.25,
        });

        L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
            maxZoom: 19,
            noWrap: true,
        }).addTo(map);

        const markersByName = new Map();

        places.forEach((place) => {
            const marker = L.marker(place.coordinates, {
                icon: markerIcon,
                keyboard: !isPreview,
                title: place.name,
            }).addTo(map);

            if (!isPreview) {
                marker.bindPopup(
                    `<strong>${place.name}</strong><span>${place.region}</span>`
                );
            }

            markersByName.set(place.name, marker);
        });

        fitMapToPlaces();

        const accordionSection = element.closest("details");

        accordionSection?.addEventListener("toggle", () => {
            if (!accordionSection.open) {
                return;
            }

            window.requestAnimationFrame(() => {
                map.invalidateSize();
                fitMapToPlaces();
            });
        });

        if (!isPreview) {
            const placeIndex = document.querySelector("[data-place-index]");

            placeIndex?.addEventListener("click", (event) => {
                const button = event.target.closest("[data-place-name]");

                if (!button) {
                    return;
                }

                const marker = markersByName.get(button.dataset.placeName);

                if (!marker) {
                    return;
                }

                map.flyTo(marker.getLatLng(), 6, { duration: 0.8 });
                marker.openPopup();
            });
        }
    });
}
