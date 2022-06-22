module.exports = {
  Admins: ["Crazy Boy#1187", "Crazy Gang"], //Admins of the bot
  ExpressServer: false,//If you wanted to make the website run or not
  DefaultPrefix: process.env.Prefix || "-", //Default prefix, Server Admins can change the prefix
  Port: 3000, //Which port website gonna be hosted
  SupportServer: "http://discord.gg/dKmEFtnbB5", //Support Server Link
  Token: process.env.Token || "ODg4ODA0MzI0NzQ1MDQ0MDQ4.YUYBiA.vbNjBd1LSiEqQPH2zeNPfDC1RCI", //Discord Bot Token
  ClientID: process.env.Discord_ClientID || "888804324745044048", //Discord Client ID
  ClientSecret: process.env.Discord_ClientSecret || "MRZZHH9WK5qTqFnklNsHUPzItMFsqE38", //Discord Client Secret
  Scopes: ["identify", "guilds", "applications.commands"], //Discord OAuth2 Scopes
  CallbackURL: "/api/callback", //Discord OAuth2 Callback URL
  "24/7": true, //If you want the bot to be stay in the vc 24/7
  CookieSecret: "demon slayer", //A Secret like a password
  IconURL:
    "https://raw.githubusercontent.com/AnshSachan/Crazy-Gang/main/Untitled-1-removebg-preview.png", //URL of all embed author icons | Dont edit unless you dont need that Music CD Spining
  Permissions: 2205280576, //Bot Inviting Permissions
  Website: process.env.Website || "http://localhost", //Website where it was hosted at includes http or https || Use "0.0.0.0" if you using Heroku

  //Lavalink
   Lavalink: {
    id: "Main",
    host: "lavalink.oops.wtf",
    port: 2000,
    pass: "www.freelavalink.ga",  
    secure: false, // Set this to true if you're self-hosting lavalink on replit.
  },
  
  //Alternate Lavalink
  /*
  Lavalink: {
    id: "Main",
    host: "lava.sudhan.tech",
    port: 1234,
    pass: "CodingWithSudhan", 
    secure: false // Set this to true if you're self-hosting lavalink on replit.
  },
  */

  //Please go to https://developer.spotify.com/dashboard/
  Spotify: {
    ClientID: process.env.Spotify_ClientID || "92d8b5dd70f64ff2a98abe6c0073fb01", //Spotify Client ID
    ClientSecret: process.env.Spotify_ClientSecret || "43b3ebd6c44f480797ef6b5116d73766", //Spotify Client Secret
  },
};
