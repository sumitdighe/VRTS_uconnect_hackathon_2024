import React, { useEffect, useState } from 'react';
import axios from 'axios';

const SampleComponent = () => {
    const [message, setMessage] = useState('');

    useEffect(() => {
        const fetchMessage = async () => {
            try {
                const response = await axios.get('http://43.204.220.52/MainApp/sample/');
                setMessage(response.data.message);
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        };

        fetchMessage();
    }, []);

    return (
        <div>
            <h2>Message from Django backend:</h2>
            <p>{message}</p>
        </div>
    );
};

export default SampleComponent;
