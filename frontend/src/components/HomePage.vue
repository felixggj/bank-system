<!-- Home Page -->
<template>
  <div id="home">
    <header>
      <nav>
        <router-link to="/" class="headerElem home">Home Page</router-link>
        <router-link to="/accounts" class="headerElem accounts"
          >Accounts</router-link
        >
        <router-link to="/skull" class="headerElem skull">Skull</router-link>
      </nav>
    </header>

    <h1 id="title">Bank System</h1>
    <p id="shortDescription">Welcome to the IE Bank!</p>
    <img src="../assets/bank.jpg" alt="Bank Logo" />

    <nav id="buttonNav">
      <router-link to="/accounts">
        <button type="button" class="btn btn-accounts">Accounts</button>
      </router-link>

      <router-link to="/skull">
        <button type="button" class="btn btn-skull">Skull</button>
      </router-link>
    </nav>
  </div>
</template>

<style scoped>
#home {
  font-family: "Arial", sans-serif;
  color: #333;
}

header {
  background-color: #09294a;
  padding: 10px;
  text-align: center;
  box-shadow: 0px 3px 10px 0px rgba(0, 0, 0, 0.1);
}

nav {
  display: flex;
  justify-content: space-around;
}

.headerElem {
  padding: 15px 25px;
  text-decoration: none;
  font-size: 18px;
  color: white;
  border-radius: 5px;
  transition: background-color 0.3s;
}

.headerElem:hover {
  background-color: #22323d;
}

#title {
  margin-top: 50px;
  font-size: 48px;
  text-align: center;
  font-weight: 800;
}

#shortDescription {
  margin-top: 10px;
  font-size: 20px;
  text-align: center;
  color: #666;
  font-weight: 500;
}

img {
  display: block;
  margin: 50px auto;
  width: 200px;
  height: 200px;
}

#buttonNav {
  display: flex;
  justify-content: center;
  margin-top: 30px;
}

.btn {
  margin: 0 15px;
  padding: 10px 20px;
  font-size: 18px;
  border: none;
  cursor: pointer;
  transition: background-color 0.3s, color 0.3s;
}

.btn-accounts {
  background-color: #007bff;
  color: white;
}

.btn-skull {
  background-color: #dc3545;
  color: white;
}

.btn:hover {
  background-color: #333;
  color: white;
}
</style>
