// Do our axios get request to poke api
// return main body of the app
// returning 6 pokemon pictures
import axios from "axios";
import { useState, useEffect } from 'react'

const Pokemon = () => {
  const [url, setUrl] = useState(null)

    const getPokemon = async () => {
      try {
        const response = await axios.get("https://pokeapi.co/api/v2/pokemon/ditto")
        console.log(response.data)
        let pokemon = response.data.sprites.front_default
        setUrl(pokemon)
      }
      catch {(error) => console.error(error)}
    }

  useEffect(() => {
    getPokemon()
  }, [])

    return (
      <>
        {url ? <img src={url}></img> : "Pokemon does not exist"}
        <p>Hello</p>
      </>
    )
}


export default Pokemon


/*

const getPokemon = async () => {
  try {
    const response = await axios.get("https://pokeapi.co/api/v2/pokemon/ditto");
    console.log(response.data.sprites.front_default);
  } catch (error) {
    console.error("An error occurred:", error);
  }
};

getPokemon();

*/