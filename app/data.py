"""Portfolio content passed to the Jinja templates."""

HOBBIES = [
    {
        "name": "Coding & Research",
        "slug": "coding-research",
        "description": (
            "Creating AI products, building personal projects, and exploring "
            "AI/ML/DL research questions."
        ),
    },
    {
        "name": "Cooking & Baking",
        "slug": "cooking-baking",
        "description": "Trying new recipes and turning kitchen ideas into side projects.",
    },
    {
        "name": "Travel",
        "slug": "travel",
        "description": "Exploring new places through their food, culture, and everyday details.",
    },
    {
        "name": "Photography",
        "slug": "photography",
        "description": "Capturing people, landscapes, and small moments worth remembering.",
    },
    {
        "name": "Painting",
        "slug": "painting",
        "description": "Slowing down, experimenting with color, and making things by hand.",
    },
]


HOBBY_SECTIONS = [
    {
        "name": "Coding & Research",
        "slug": "coding-research",
        "intro": (
            "Selected software projects and research I've done over the years, spanning Applied AI, "
            "ML systems, distributed systems, and Networking."
        ),
        "kind": "projects",
        "items": [
            {
                "title": "SmartPantry",
                "label": "Full-stack AI product",
                "caption": (
                    "A pantry inventory and recipe platform combining "
                    "computer vision, learned ranking, and grounded AI workflows."
                ),
                "tech": "Next.js · FastAPI · PostgreSQL · YOLOv8 · XGBoost · RAG · AWS · Docker",
                "theme": "pantry",
                "links": [
                    {
                        "label": "Live demo",
                        "url": "https://smart-pantry-xi.vercel.app",
                    },
                    {
                        "label": "GitHub",
                        "url": "https://github.com/helia295/SmartPantry",
                    },
                ],
            },
            {
                "title": "Syncode",
                "label": "Distributed systems",
                "caption": (
                    "A Git-like distributed version control system with "
                    "branching, synchronization, merge workflows, and a Rust CLI."
                ),
                "tech": "Rust · CLI · Filesystems · Distributed systems",
                "theme": "terminal",
                "links": [
                    {
                        "label": "GitHub",
                        "url": "https://github.com/helia295/syncode",
                    },
                ],
            },
            {
                "title": "Music Streaming App",
                "label": "Networking project",
                "caption": (
                    "A Python client-server application for search, download, "
                    "buffered playback, and real-time audio delivery over TCP."
                ),
                "tech": "Python · TCP sockets · PyAudio · ffmpeg",
                "theme": "audio",
                "links": [
                    {
                        "label": "GitHub",
                        "url": "https://github.com/helia295/music-client-server-app",
                    },
                ],
            },
            {
                "title": "Structured Data Gradient Pruning",
                "label": "ICPR 2022 research",
                "caption": (
                    "A structured sparsity method for accelerating neural "
                    "network training while preserving convergence behavior on GPUs."
                ),
                "tech": "Deep learning · Structured sparsity · CUDA",
                "theme": "paper",
                "links": [
                    {
                        "label": "Read paper",
                        "url": "https://arxiv.org/abs/2202.00774",
                    },
                    {
                        "label": "Research code",
                        "url": "https://github.com/BradMcDanel/sdgp",
                    },
                ],
            },
        ],
    },
    {
        "name": "Cooking & Baking",
        "slug": "cooking-baking",
        "intro": "Recipe experiments, favorite bakes, and the occasional beautiful mess.",
        "kind": "gallery",
        "items": [
            {
                "image": "hobbies/cooking/cookies.webp",
                "alt": "Homemade cookies",
                "caption": "I make really good choco chips cookies :)",
            },
            {
                "image": "hobbies/cooking/nem.webp",
                "alt": "Nem (Vietnamese fried rolls) making",
                "caption": "Professionally folding nem (Vietnamese fried spring rolls) with friends.",
            },
            {
                "image": "hobbies/cooking/strawberry_redvelvet.webp",
                "alt": "Homemade red velvet cake decorated with fresh strawberry",
                "caption": "A strawberry red velvet cake I baked for a friend gathering.",
            },
            {
                "image": "hobbies/cooking/croissant.webp",
                "alt": "Croissants served beside a floral teapot and teacup",
                "caption": "A quiet tea break with freshly baked croissants.",
            },
            {
                "image": "hobbies/cooking/eggtart.webp",
                "alt": "Egg tarts baking on a tray in the oven",
                "caption": "Watching a batch of egg tarts puff up in the oven.",
            },
            {
                "image": "hobbies/cooking/ramen_jjajang.webp",
                "alt": "Spicy ramen and jjajang noodles served together",
                "caption": "A Korean-inspired comfort-food night with friends.",
            },
        ],
    },
    {
        "name": "Travel",
        "slug": "travel",
        "intro": (
            "Places, food, and everyday details collected along the way. "
            "A travel map will join this section in a later update."
        ),
        "kind": "gallery",
        "items": [
            {
                "image": "hobbies/travel/biking_kauai.webp",
                "alt": "Friends taking a break during a bike ride in Kauai",
                "caption": "Exploring Kauai by bike with friends.",
            },
            {
                "image": "hobbies/travel/helicopter_napali.webp",
                "alt": "View from a helicopter flying above the Na Pali Coast",
                "caption": "Seeing the Na Pali Coast from above.",
            },
            {
                "image": "hobbies/travel/kauai_sunset.webp",
                "alt": "Watching the sun set over the ocean in Kauai",
                "caption": "A golden sunset by the water in Kauai.",
            },
            {
                "image": "hobbies/travel/locomoco.webp",
                "alt": "Plates of loco moco and other Hawaiian food",
                "caption": "Trying loco moco and local comfort food in Hawaii.",
            },
            {
                "image": "hobbies/travel/puu_poa_beach.webp",
                "alt": "Friends standing in the shallow water at Puu Poa Beach",
                "caption": "A beach day with friends at Puu Poa Beach, Kauai.",
            },
            {
                "image": "hobbies/travel/lamberton.webp",
                "alt": "Friends visiting a tropical conservatory",
                "caption": "An afternoon among the plants at Lamberton Conservatory (Rochester, NY).",
            },
            {
                "image": "hobbies/travel/singapore.webp",
                "alt": "Jubilee Walk marker on a sidewalk in Singapore",
                "caption": "Following the Jubilee Walk through Singapore.",
            },
        ],
        "reserved_feature": "travel-map",
    },
    {
        "name": "Photography",
        "slug": "photography",
        "intro": "Portraits, landscapes, and small moments that caught my attention.",
        "kind": "gallery",
        "items": [
            {
                "image": "hobbies/photography/hangout.webp",
                "alt": "Shadows of friends cast across grass and flowers",
                "caption": "A sunny afternoon remembered through shadows (Rochester, NY).",
            },
            {
                "image": "hobbies/photography/hanoi_hoguom.webp",
                "alt": "Red bridge crossing Hoan Kiem Lake in Hanoi",
                "caption": "A quiet view across Hoan Kiem Lake in Hanoi, VN.",
            },
            {
                "image": "hobbies/photography/holga2.webp",
                "alt": "Yellow car framed through an autumn leaf",
                "caption": "Playing with perspective, autumn color, and a yellow Mini (taken with Holga film @Lancaster, PA).",
            },
            {
                "image": "hobbies/photography/rugby.webp",
                "alt": "Players competing during an outdoor rugby match",
                "caption": "Freezing a fast moment during a college rugby match (Lancaster, PA).",
            },
            {
                "image": "hobbies/photography/starry_sky_kauai.webp",
                "alt": "Stars visible above a silhouetted tree in Kauai",
                "caption": "A starry night through the trees in Kauai.",
            },
            {
                "image": "hobbies/photography/thean_hou_temple_malaysia.webp",
                "alt": "Lanterns hanging above the courtyard at Thean Hou Temple",
                "caption": "Lanterns and afternoon light at Thean Hou Temple (Malaysia).",
            },
        ],
    },
    {
        "name": "Painting",
        "slug": "painting",
        "intro": "A healing creative hobby built around color, texture, and curiosity.",
        "kind": "gallery",
        "items": [
            {
                "image": "hobbies/painting/flower.webp",
                "alt": "Mixed-media floral cityscape painting in progress",
                "caption": "A floral cityscape taking shape on my desk.",
            },
            {
                "image": "hobbies/painting/night_sky.webp",
                "alt": "Night-sky painting with clouds, trees, and a crescent moon",
                "caption": "Experimenting with clouds, silhouettes, and moonlight.",
            },
        ],
    },
]
EDUCATION = [
    {
        "title": "M.S. in Computer Science · AI Track",
        "organization": "University of Rochester",
        "dates": "August 2023 – December 2025",
        "description": (
            "Focused on scalable machine learning, data-centric AI, computer "
            "vision, human-inspired AI, and distributed training. GPA: 3.9/4.0."
        ),
    },
    {
        "title": "B.A. in Computer Science · B.A. in Business, Organizations & Society",
        "organization": "Franklin & Marshall College",
        "dates": "August 2019 – May 2023",
        "description": (
            "Combined software engineering and AI research with an "
            "interdisciplinary foundation in business and organizations. "
            "GPA: 3.8/4.0."
        ),
    },
]
EXPERIENCES = [
    {
        "title": "MLE Expert Writer",
        "organization": "Mercor",
        "dates": "June 2026 – Present",
        "description": (
            "Develop competitive, reproducible reference solutions for "
            "real-world machine learning benchmarks, with careful validation, "
            "leakage checks, and reviewer-ready code."
        ),
    },
    {
        "title": "Production Engineering Fellow/Intern",
        "organization": "MLH Fellowship · Meta",
        "dates": "June 2026 – September 2026",
        "description": (
            "Build practical production engineering skills through projects, "
            "technical collaboration, and guidance from experienced engineers from Meta."
        ),
    },
    {
        "title": "AI Trainer · Software Engineering Specialist",
        "organization": "Handshake AI",
        "dates": "April 2026 – June 2026",
        "description": (
            "Evaluated LLM-generated code and tests, developed golden "
            "solutions, and identified correctness gaps and missing edge cases."
        ),
    },
    {
        "title": "Graduate Research Assistant · Scalable & Data-Centric AI",
        "organization": "University of Rochester",
        "dates": "August 2023 – December 2025",
        "description": (
            "Built reproducible infrastructure for large-scale deep learning "
            "experiments, including distributed multi-GPU workflows, "
            "checkpointing, monitoring, and data-centric analysis."
        ),
    },
    {
        "title": "Graduate Teaching Assistant",
        "organization": "University of Rochester",
        "dates": "January 2024 – December 2025",
        "description": (
            "Led hands-on labs and supported 100+ students across "
            "Computational Neuroscience, Data Mining, and Advanced Algorithms "
            "through lectures, grading, office hours, and mentorship."
        ),
    },
    {
        "title": "Data Science Intern",
        "organization": "VNPAY Solutions",
        "dates": "June 2022 – August 2022",
        "description": (
            "Built web scraping, data, and fraud detection pipelines to automate risk analysis across 3,000+ merchant sites, created an "
            "internal Flask-backed monitoring dashboard, reducing manual workloads and improving efficiency significantly."
        ),
    },
    {
        "title": "Computer Science Research Assistant · Deep Learning Optimization",
        "organization": "Franklin & Marshall College",
        "dates": "June 2021 – March 2022",
        "description": (
            "Researched structured gradient pruning for faster neural network "
            "training, achieving 15–25% speedups in evaluated experiments and "
            "co-authoring a peer-reviewed ICPR 2022 paper."
        ),
    },
    {
        "title": "AI/ML Engineer Intern",
        "organization": "Viettel Solutions",
        "dates": "July 2020 – December 2020",
        "description": (
            "Trained and evaluated a computer vision model on more than "
            "500,000 images, improving robustness through architecture tuning, "
            "data cleanup, and automated preprocessing."
        ),
    },
]
