<template>
    <div class="error">
        <h1>404 ERROR:</h1>
        <h3>The selected resource does not exist or you do not have access to it.</h3>
        <router-link to="/">Back to Home</router-link>
    </div>
</template>

<script>
export default {
    name: "PNF"
};
</script>

<style scoped>
.error {
    display: flex;
    flex-direction: column;
    margin-top: 100px;
}

.error > h1 {
    letter-spacing: 1px;
    margin-bottom: 12px;
}

.error > a {
    background-color: var(--color-primary-contrast);
    width: 140px;
    margin-left: auto;
    margin-right: auto;
    padding-top: 6px;
    padding-bottom: 6px;
    border-radius: 4px;
    box-shadow: 2px 2px 2px var(--color-shadow);
    color: white;
    text-decoration: none;
    font-family: 'Open Sans', sans-serif;
    letter-spacing: 1px;
    margin-top: 12px;
}

.error > a:active {
    box-shadow: 3px 3px 2px var(--color-shadow);
}
</style>
