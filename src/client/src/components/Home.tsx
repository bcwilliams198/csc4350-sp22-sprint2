import React, { useEffect, useState } from 'react'
import { Nav } from './Navbar';
import Button from "react-bootstrap/Button";

interface UserApi {
    name: string,
    email: string,
    picture: string
}

export const Home: React.FunctionComponent = () => {
    const [data, setData] = useState<UserApi>()
    useEffect(() => {
        fetch('/get_user_info')
            .then(response => {
                return response.json()
            }).then(response => setData(response))
    }, [])
    return (
        <div className="Homepage">
            <div className="navbar">{renderNavbar()}</div>
            <div className="Home">
                <h1> The Pokedex </h1>
                <br></br>
                <div className="slides">
                    <div id="mySlide" className="carousel slide" data-bs-ride="carousel">
                        <div className="carousel-inner">
                            <div className="carousel-item active">
                                <h2>Pick Your Team!</h2>
                                <img src="/static/team.png" className="d-block w-100" alt="Your Team"></img>
                            </div>
                            <div className="carousel-item">
                                <h2>Search for Pokemon!</h2>
                                <img src="/static/pokemoncards.png" className="d-block w-100" alt="Search"></img>
                            </div>
                            <div className="carousel-item">
                                <h2>This is yours!</h2>
                                <img src="/static/pokemon.png" className="d-block w-100" alt="Pokemon"></img>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
    function renderNavbar() {
        if (data !== undefined) {
            console.log("I am not undefined")
            return (
                <Nav user={data} />
            )
        }
        console.log("I am undefined")
        return (
            <div>
                <nav className="navbar navbar-dark bg-dark">
                    <div className="container-fluid">

                        <a className="nav-link active" aria-current="page" href="/">The Pokedex</a>

                        <a className="nav-link active" href="/search">Search</a>

                        <a className="nav-link active" href="/teams">Team</a>

                        <a className="nav-link active" href="/logout">Logout</a>

                    </div>
                </nav>
            </div>
        );
    }

}
