<template>
    <div class="splash">
        <div class="splash-text">
            <h1>Welcome to knotelry</h1>
            <h2>Your home for your crafts</h2>
            <h3>...yes, ALL of them</h3>
        </div>
        <img src="https://knotelry.s3.amazonaws.com/splash_1.jpg" />
    </div>
    <div class="home-body">
        <div class="home-sidebar">
            <div class="sidebar-section">
                <p class="header">Quick Browse:</p>
                <div class="quick-browse-options">
                    <!-- These will eventually redirect to category pages for crafts -->
                    <p class="craft-button">spinning</p>
                    <!-- <p class="craft-button">weaving</p> -->
                    <p class="craft-button">knitting</p>
                    <!-- <p class="craft-button">crocheting</p> -->
                    <p class="craft-button">sewing</p>
                    <!-- <p class="craft-button">embroidery</p> -->
                </div>
            </div>
        </div>
        <div class="home-blogs">
            <div class="blog-post">
                <div class="blog-meta-container">
                    <p class="title">Sample Blog Post</p>
                    <div class="blog-meta">
                        <div>
                            <p>By knitboop</p>
                            <p>March 20, 2022</p>
                        </div>
                        <img
                            src="https://qqc.s3.amazonaws.com/profilepic_1.jpg"
                            alt="Blog author image"
                        />
                    </div>
                </div>

                <p>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                    Vivamus ac elit nisi. Quisque efficitur efficitur mi,
                    pulvinar tincidunt velit rhoncus eget. Pellentesque non
                    viverra sapien, at euismod justo. Suspendisse ullamcorper id
                    nisi sed lobortis. Morbi sollicitudin pulvinar sollicitudin.
                    Suspendisse non augue quis erat faucibus hendrerit quis sit
                    amet urna. Praesent tempus massa est, semper pellentesque
                    dolor varius eget. Nunc et nibh ac tellus mollis volutpat ac
                    eget diam.
                    <br />
                    <br />
                    Proin mi purus, aliquet vel sapien vel, cursus pellentesque
                    arcu. Suspendisse potenti. Proin et sem ut dui sollicitudin
                    commodo. Etiam sagittis augue vitae mi tincidunt commodo.
                    Duis viverra euismod porta. Vivamus volutpat mollis elit, a
                    commodo arcu facilisis a. Aliquam ac ultrices sapien. Nulla
                    pretium augue ex, sit amet rutrum ex condimentum a. Mauris
                    commodo venenatis consectetur. Mauris molestie ac turpis eu
                    viverra. Quisque pharetra ultrices vestibulum. Vestibulum
                    tristique ipsum ac eleifend volutpat. Aenean dapibus, nisi
                    sed consequat pharetra, est nunc convallis quam, nec
                    facilisis libero leo et justo. Vestibulum in lacus eget mi
                    condimentum consectetur.
                </p>
            </div>
            <div class="blog-post">
                <div class="blog-meta-container">
                    <p class="title">Another Lil' Bloggy Blog</p>
                    <div class="blog-meta">
                        <div>
                            <p>By not-knitboop</p>
                            <p>March 22, 2022</p>
                        </div>
                        <img
                            src="https://qqc.s3.amazonaws.com/profilepic_default.png"
                            alt="Blog author image"
                        />
                    </div>
                </div>

                <p>
                    Nulla facilisi. Sed sem purus, eleifend et aliquet sit amet,
                    suscipit vel felis. Vestibulum rutrum urna et pulvinar
                    euismod. Morbi vitae dolor ex. Aenean vulputate posuere nibh
                    vel pharetra. Maecenas non ligula pharetra, accumsan odio
                    vel, dapibus tellus. Curabitur eget nulla eu ex molestie
                    tempus eu quis augue. Suspendisse rutrum urna in felis
                    interdum auctor. Vivamus vitae felis accumsan, gravida nisl
                    vitae, suscipit nulla. Nullam id neque commodo neque congue
                    congue. In nec nibh a orci venenatis dapibus vel ac turpis.
                    Cras tristique vestibulum ornare. Cras accumsan id neque a
                    tristique. Praesent varius tellus nec ullamcorper faucibus.
                </p>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "Home",
};
</script>

<style scoped>
.splash {
    background-color: white;
    height: 360px;
    padding-left: 12%;
    padding-right: 12%;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
}

.splash-text {
    text-align: left;
    align-content: center;
    letter-spacing: 1px;
}

.splash-text > h1 {
    color: var(--color-primary-contrast);
    font-family: "Pacifico", serif;
    font-weight: normal;
    font-size: 50px;
    margin-bottom: -18px;
}

.splash > img {
    object-fit: contain;
    height: 320px;
}

.home-body {
    margin-left: 12%;
    margin-right: 12%;
    margin-bottom: 36px;
    display: grid;
    grid-template-columns: 200px 1fr;
    column-gap: 24px;
}

.home-sidebar {
    width: 200px;
    margin-top: 36px;
}

.sidebar-section {
    border: 1px solid var(--color-shadow);
    border-radius: 4px;
    box-shadow: 2px 2px 2px var(--color-shadow);
    background-color: white;
}

.sidebar-section > .header {
    background-color: var(--color-primary-contrast);
    margin-top: 0px;
    padding-top: 8px;
    padding-bottom: 8px;
    color: white;
    font-family: "Open Sans", sans-serif;
    letter-spacing: 1px;
}

.quick-browse-options {
    letter-spacing: 1px;
    font-size: 13px;
    margin-bottom: 4px;
    margin-top: -2px;
}

.craft-button:hover {
    font-weight: bold;
    cursor: pointer;
}

.home-blogs {
    text-align: justify;
    margin-top: 12px;
    margin-left: 5%;
    margin-right: 5%;
}

.blog-post {
    margin: 24px;
    background-color: white;
    padding: 24px;
    border-radius: 12px;
    box-shadow: 2px 2px 2px var(--color-shadow);
    border: 1px solid var(--color-shadow);
}

.blog-meta-container {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
}

.blog-meta-container > .blog-meta {
    font-size: 13px;
    display: flex;
    flex-direction: row;
    align-items: center;
    column-gap: 12px;
}

.blog-meta > img {
    width: 50px;
    height: 50px;
    border-radius: 4px;
    border: 1px solid var(--color-shadow);
}

.blog-meta > div > p {
    margin-top: 4px;
    margin-bottom: 4px;
}

.blog-meta-container > .title {
    font-weight: bold;
    font-size: 32px;
    margin: 0px;
}

.blog-post > p {
    font-size: 15px;
}
</style>
