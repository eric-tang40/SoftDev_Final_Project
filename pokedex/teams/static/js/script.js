
const teams = {
    brock: ["Onix", "Geodude", "Sandslash", "Kabutops", "Rhyhorn", "Graveler"],
    misty: ["Starmie", "Psyduck", "Golduck", "Staryu", "Gyarados", "Psyduck"],
    surge: ["Voltorb", "Pikachu", "Raichu", "Magnemite", "Electabuzz", "Jolteon"], 
    erika: ["Victreebell", "Tangela", "Vileplume", "Leafeon", "Exeggcute", "Oddish"],
    koga: ["Koffing", "Muk", "Weezing", "Venomoth", "Crobat", "Ariados"],
    sabrina: ["Kadabra", "Drowzee", "Mr. Mime", "Espeon", "Alakazam", "Slowbro"],
    giovanni: ["Nidoking", "Garchomp", "Dugtrio", "Rhydon", "Persian", "Mewtwo"]
   
};

// ****IMAGES ARE NOT WORKING***** 
const gymLeadersData = {
    brock: {
        team: ["Onix", "Geodude", "Sandslash", "Kabutops", "Rhyhorn", "Graveler"],
        image: "/static/img/brock.png", 
    },
    misty: {
        team: ["Starmie", "Psyduck", "Golduck", "Staryu", "Gyarados", "Psyduck"],
        image: "/static/img/misty.png", 
    },
    surge: {
        team: ["Voltorb", "Pikachu", "Raichu", "Magnemite", "Electabuzz", "Jolteon"], 
        image: "/static/img/surge.png", 
    },
    erika: {
        team: ["Victreebell", "Tangela", "Vileplume", "Leafeon", "Exeggcute", "Oddish"],
        image: "/static/img/erika.png", 
    },
    koga: {
        team: ["Koffing", "Muk", "Weezing", "Venomoth", "Crobat", "Ariados"],
        image: "/static/img/koga.png", 
    },
    sabrina: {
        team: ["Kadabra", "Drowzee", "Mr. Mime", "Espeon", "Alakazam", "Slowbro"],
        image: "/static/img/sabrina.png", 
    },
    giovanni: {
        team: ["Nidoking", "Garchomp", "Dugtrio", "Rhydon", "Persian", "Mewtwo"],
        image: "/static/img/giovanni.png", 
    },
    
};

function displayTeam(gymLeader) {
    const gymLeadersContainer = document.getElementById("gymLeaders");

    gymLeadersContainer.innerHTML = "";

    // team
    const teamSection = document.createElement("section");
    teamSection.id = "teamContainer";  // Use a consistent ID for the team container
    
    const teamList = gymLeadersData[gymLeader].team;
    const teamTitle = document.createElement("h2");
    teamTitle.textContent = `${gymLeader.charAt(0).toUpperCase() + gymLeader.slice(1)}'s Team`;
    teamSection.appendChild(teamTitle);

    teamList.forEach(pokemon => {
        const pokemonElement = document.createElement("p");
        pokemonElement.textContent = pokemon;
        teamSection.appendChild(pokemonElement);
    });

    gymLeadersContainer.appendChild(teamSection);

    // img
    const imageContainer = document.createElement("div");
    imageContainer.id = "gymLeaderImage"; // Keep this ID consistent for styling
    const image = document.createElement("img");
    image.src = gymLeadersData[gymLeader].image;
    image.alt = `${gymLeader.charAt(0).toUpperCase() + gymLeader.slice(1)}'s Image`;
    imageContainer.appendChild(image);

    gymLeadersContainer.appendChild(imageContainer);
}

// buttons
const buttonsContainer = document.getElementById("buttons");

for (const gymLeader in gymLeadersData) {
    const button = document.createElement("button");
    button.textContent = `${gymLeader.charAt(0).toUpperCase() + gymLeader.slice(1)}`;
    button.addEventListener("click", () => displayTeam(gymLeader));
    buttonsContainer.appendChild(button);
}

// hide initial content
const contentSections = document.querySelectorAll("#gymLeaders section, #gymLeaderImage");
contentSections.forEach(section => {
    section.style.display = "none";
});