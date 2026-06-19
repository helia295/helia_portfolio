const sections = Array.from(document.querySelectorAll(".accordion-section"));

function openSectionFromHash() {
    const id = window.location.hash.slice(1);
    const target = id ? document.getElementById(id) : null;

    if (!(target instanceof HTMLDetailsElement)) {
        return;
    }

    sections.forEach((section) => {
        section.open = section === target;
    });

    window.requestAnimationFrame(() => {
        target.scrollIntoView({ block: "start" });
    });
}

sections.forEach((section) => {
    section.addEventListener("toggle", () => {
        if (!section.open) {
            return;
        }

        sections.forEach((otherSection) => {
            if (otherSection !== section) {
                otherSection.open = false;
            }
        });

        window.history.replaceState(null, "", `#${section.id}`);
    });
});

window.addEventListener("hashchange", openSectionFromHash);
openSectionFromHash();
