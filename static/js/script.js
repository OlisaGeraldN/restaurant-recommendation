// script.js
document.getElementById("recommendation-form").addEventListener("submit", async function (event) {
    event.preventDefault();
    const location = document.getElementById("location").value;
    const cuisine = document.getElementById("cuisine").value;

    const response = await fetch(`/api/recommendations?location=${location}&cuisine=${cuisine}`);
    const data = await response.json();

    const resultsDiv = document.getElementById("results");
    resultsDiv.innerHTML = "";

    if (data.length > 0) {
        const heading = document.createElement("h2");
        heading.textContent = "Restaurant Recommendations:";
        resultsDiv.appendChild(heading);

        const ul = document.createElement("ul");
        for (const restaurant of data) {
            const li = document.createElement("li");
            li.textContent = `${restaurant.name} - Rating: ${restaurant.rating} - ${restaurant.location.address1}`;
            ul.appendChild(li);
        }
        resultsDiv.appendChild(ul);
    } else {
        const message = document.createElement("p");
        message.textContent = "No restaurants found matching your preferences.";
        resultsDiv.appendChild(message);
    }
});
