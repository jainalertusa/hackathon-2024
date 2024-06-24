const express = require('express');
const axios = require('axios');
const cors = require('cors');

const app = express();
const port = 8000;

app.use(cors());

const API_KEY = "035e4b738dd6431690a67690c0a3865e";
const BASE_URL = "https://api.gateway.attomdata.com/propertyapi/v1.0.0/property/address";
const DETAIL_URL = "https://api.gateway.attomdata.com/propertyapi/v1.0.0/property/detailowner";

app.get('/property', async (req, res) => {
    const { postalcode, page = 1, pagesize = 100 } = req.query;

    const headers = {
        'Accept': 'application/json',
        'apikey': API_KEY,
    };

    const params = {
        postalcode: postalcode,
        page: page,
        pagesize: pagesize,
    };

    try {
        const response = await axios.get(BASE_URL, { headers, params });
        res.json(response.data);
    } catch (error) {
        res.status(error.response ? error.response.status : 500).json({
            error: 'Error fetching data from API',
        });
    }
});

app.get('/property/detail', async (req, res) => {
    const { attomId } = req.query;

    const headers = {
        'Accept': 'application/json',
        'apikey': API_KEY,
    };
    console.log(attomId);

    const params = {
        attomid: attomId,
    };

    try {
        const response = await axios.get(DETAIL_URL, { headers, params });
        res.json(response.data);
    } catch (error) {
        console.log(error.response);
        res.status(error.response ? error.response.status : 500).json({
            error: 'Error fetching property details from API',
        });
    }
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
