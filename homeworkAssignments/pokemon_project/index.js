import axios from "axios";

console.log("Hello Axios");


const getPokemon = async () => {
    const url = "https://pokeapi.co/api/vs/pokemon/ditto"

    try {
        const response = await axios.get(url);
        console.log(response.data.sprites.front_default);

    } catch(error) {
        console.log("Error", error);
    }

}

getPokemon();