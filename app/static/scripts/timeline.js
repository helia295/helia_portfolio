const timelineForm = document.querySelector("#timeline-form");
const timelinePosts = document.querySelector("#timeline-posts");
const timelineStatus = document.querySelector("#timeline-status");
const refreshButton = document.querySelector("#timeline-refresh");

function md5(input) {
    function rotateLeft(value, shift) {
        return (value << shift) | (value >>> (32 - shift));
    }

    function addUnsigned(a, b) {
        const a4 = a & 0x40000000;
        const b4 = b & 0x40000000;
        const a8 = a & 0x80000000;
        const b8 = b & 0x80000000;
        const result = (a & 0x3fffffff) + (b & 0x3fffffff);

        if (a4 & b4) {
            return result ^ 0x80000000 ^ a8 ^ b8;
        }

        if (a4 | b4) {
            if (result & 0x40000000) {
                return result ^ 0xc0000000 ^ a8 ^ b8;
            }

            return result ^ 0x40000000 ^ a8 ^ b8;
        }

        return result ^ a8 ^ b8;
    }

    function convertToWordArray(value) {
        const messageLength = value.length;
        const wordCount = (((messageLength + 8) - ((messageLength + 8) % 64)) / 64 + 1) * 16;
        const wordArray = Array(wordCount - 1).fill(0);

        for (let i = 0; i < messageLength; i += 1) {
            wordArray[i >> 2] |= value.charCodeAt(i) << ((i % 4) * 8);
        }

        wordArray[messageLength >> 2] |= 0x80 << ((messageLength % 4) * 8);
        wordArray[wordCount - 2] = messageLength << 3;
        wordArray[wordCount - 1] = messageLength >>> 29;

        return wordArray;
    }

    function wordToHex(value) {
        let hex = "";

        for (let i = 0; i <= 3; i += 1) {
            const byte = (value >>> (i * 8)) & 255;
            hex += `0${byte.toString(16)}`.slice(-2);
        }

        return hex;
    }

    const utf8Input = unescape(encodeURIComponent(input));
    const words = convertToWordArray(utf8Input);

    let a = 0x67452301;
    let b = 0xefcdab89;
    let c = 0x98badcfe;
    let d = 0x10325476;

    const s = [
        7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
        5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20,
        4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
        6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21,
    ];
    const k = Array.from({ length: 64 }, (_, index) => Math.floor(Math.abs(Math.sin(index + 1)) * 4294967296));

    for (let i = 0; i < words.length; i += 16) {
        const aa = a;
        const bb = b;
        const cc = c;
        const dd = d;

        for (let j = 0; j < 64; j += 1) {
            let f;
            let g;

            if (j < 16) {
                f = (b & c) | ((~b) & d);
                g = j;
            } else if (j < 32) {
                f = (d & b) | ((~d) & c);
                g = (5 * j + 1) % 16;
            } else if (j < 48) {
                f = b ^ c ^ d;
                g = (3 * j + 5) % 16;
            } else {
                f = c ^ (b | (~d));
                g = (7 * j) % 16;
            }

            const temp = d;
            d = c;
            c = b;
            b = addUnsigned(
                b,
                rotateLeft(addUnsigned(addUnsigned(a, f), addUnsigned(k[j], words[i + g])), s[j])
            );
            a = temp;
        }

        a = addUnsigned(a, aa);
        b = addUnsigned(b, bb);
        c = addUnsigned(c, cc);
        d = addUnsigned(d, dd);
    }

    return `${wordToHex(a)}${wordToHex(b)}${wordToHex(c)}${wordToHex(d)}`;
}

function setStatus(message, type = "neutral") {
    timelineStatus.textContent = message;
    timelineStatus.dataset.status = type;
}

function formatDate(value) {
    const date = new Date(value);

    if (Number.isNaN(date.getTime())) {
        return "Just now";
    }

    return new Intl.DateTimeFormat("en", {
        dateStyle: "medium",
        timeStyle: "short",
    }).format(date);
}

function gravatarUrl(email) {
    const normalizedEmail = email.trim().toLowerCase();
    const emailHash = md5(normalizedEmail);

    return `https://www.gravatar.com/avatar/${emailHash}?s=96&d=identicon&r=g`;
}

function renderEmptyState(message, detail) {
    timelinePosts.innerHTML = `
        <article class="timeline-empty">
            <h3>${message}</h3>
            <p>${detail}</p>
        </article>
    `;
}

function renderPosts(posts) {
    if (!posts.length) {
        renderEmptyState(
            "No posts yet.",
            "Be the first to leave a note on the timeline."
        );
        return;
    }

    timelinePosts.innerHTML = posts.map((post) => `
        <article class="timeline-post">
            <img
                class="timeline-avatar"
                src="${gravatarUrl(post.email)}"
                alt=""
                loading="lazy"
            >
            <div class="timeline-post-body">
                <div class="timeline-post-meta">
                    <h3>${escapeHtml(post.name)}</h3>
                    <time datetime="${escapeHtml(post.created_at)}">
                        ${formatDate(post.created_at)}
                    </time>
                </div>
                <p>${escapeHtml(post.content)}</p>
            </div>
        </article>
    `).join("");
}

function escapeHtml(value) {
    return String(value)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
}

async function loadTimelinePosts() {
    try {
        const response = await fetch("/api/timeline_post", {
            headers: { Accept: "application/json" },
        });

        if (!response.ok) {
            throw new Error("Could not load timeline posts.");
        }

        const data = await response.json();
        renderPosts(data.timeline_posts || []);
    } catch (error) {
        renderEmptyState(
            "Timeline unavailable.",
            "Please check the Flask server and MySQL connection, then refresh."
        );
    }
}

async function submitTimelinePost(event) {
    event.preventDefault();

    const formData = new FormData(timelineForm);
    const submitButton = timelineForm.querySelector("button[type='submit']");

    submitButton.disabled = true;
    setStatus("Posting your update…");

    try {
        const response = await fetch("/api/timeline_post", {
            method: "POST",
            body: formData,
        });

        if (!response.ok) {
            throw new Error("Could not save timeline post.");
        }

        timelineForm.reset();
        setStatus("Posted! The timeline has been refreshed.", "success");
        await loadTimelinePosts();
    } catch (error) {
        setStatus("Something went wrong. Please try again.", "error");
    } finally {
        submitButton.disabled = false;
    }
}

timelineForm.addEventListener("submit", submitTimelinePost);
refreshButton.addEventListener("click", loadTimelinePosts);

loadTimelinePosts();
