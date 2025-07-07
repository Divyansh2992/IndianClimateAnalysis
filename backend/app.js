const express=require("express");
const cors = require("cors");
const app=express();
const fs = require('fs');
const path = require('path');
const epwRoutes = require('./routes/epw');

// Allow only your Netlify frontend
const allowedOrigins = ['https://indianclimateanalysis.netlify.app'];

app.use(cors({
  origin: allowedOrigins,
  credentials: true, // if you use cookies or auth headers
}));
app.use(express.json());
app.use('/api/epw', epwRoutes);

app.listen(3000,()=>{
    console.log("Server is listening on port 3000");
})