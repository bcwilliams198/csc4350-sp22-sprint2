import React from 'react'

type CardProps = {
    user: {
        name: string,
        email: string,
        picture: string
    }
}

export const Nav: React.FunctionComponent<CardProps> = ({ user }) => {
    console.log(user)
    console.log(typeof (user))
    return (
        <div>

            <nav className="navbar navbar-dark bg-dark">
                <div className="container-fluid">
                    <a className="navbar-brand" href="/">
                        <img src="{user.picture}" alt="" width="30" height="24" className="d-inline-block align-text-top"></img>
                        <p>{user.name}</p>
                    </a>
                    <a className="nav-link active" aria-current="page" href="/">The Pokedex</a>

                    <a className="nav-link active" href="/search">Search</a>

                    <a className="nav-link active" href="/teams">Team</a>

                    <a className="nav-link active" href="/logout">Logout</a>

                </div>
            </nav>
        </div>
    )


}

