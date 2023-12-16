import React, { useEffect, useState } from "react";
import Button from 'react-bootstrap/Button';
import ButtonGroup from 'react-bootstrap/ButtonGroup';
import Dropdown from 'react-bootstrap/Dropdown';

function ChooseTeam() {

    const [team, setTeam] = useState([]);

    useEffect(() => {
        async function fetchTeams() {
            try {
                const response = await axios.get('/supported/TeamsList');
                setTeam(response.data);
            } catch(err) {
                console.log(err);
            }
        }
        fetchTeams();
    }, []);


    return (
        <Dropdown as={ButtonGroup}>
            <Button variant="success">Choose Team</Button>

            <Dropdown.Toggle split variant="success" id="dropdown-split-basic" />

            <Dropdown.Menu>
                <Dropdown.Item href="#/action-1">Action</Dropdown.Item>
                <Dropdown.Item href="#/action-2">Another action</Dropdown.Item>
                <Dropdown.Item href="#/action-3">Something else</Dropdown.Item>
            </Dropdown.Menu>
        </Dropdown>
    );
}

export default SplitBasicExample;