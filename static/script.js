async function scanURL() {

    const url = document.getElementById("urlInput").value.trim();

    const result = document.getElementById("result");

    if (!url) {
        result.innerHTML = "Please enter a URL!";
        return;
    }

    result.innerHTML = "Scanning URL...";

    try {

        const response = await fetch("/scan", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({ url: url })

        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "Scanning failed");
        }

        result.innerHTML =
            `<pre>${JSON.stringify(data, null, 2)}</pre>`;

    } catch (error) {

        result.innerHTML = "Error: " + error.message;

    }
}