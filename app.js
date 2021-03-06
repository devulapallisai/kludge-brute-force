const express = require("express");
const bodyParser = require("body-parser");
// const urlencoded = require("body-parser/lib/types/urlencoded");

const app = express();
app.set("view engine", "ejs");

app.use(express.static("public"));

app.use(bodyParser.json(), bodyParser.urlencoded({ extended: false }));
const PORT = process.config.env || 5000;

app.get("/", (req, res) => {
  res.render("./login");
});

// app.get("/");
app.get("/admin", (req, res) => {
  res.render("./loggedin");
});
app.post("/postpassword", (req, res) => {
  const correctpassword = "dude92";
  const { username, password } = req.body;
  // console.log(username, password);
  if (password === correctpassword) {
    res
      .status(200)
      .send(
        '<!DOCTYPE html><html><head><meta http-equiv="refresh" content="0; url=/admin"></head></html>'
      );
  } else {
    res
      .status(400)
      .send(
        '<!DOCTYPE html><html><head><meta http-equiv="refresh" content="0; url=/"></head></html>'
      );
  }
});

app.listen(PORT, () => {
  console.log(`Server listening on http://localhost:${PORT}`);
});
