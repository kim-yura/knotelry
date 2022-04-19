<template>
    <div class="stash-page">
        <div class="stash-page-left">
            <form class="stash-search-container" @submit.prevent="submit">
                <p class="header">Search Options</p>
                <div>
                    <label>Search by Title or Description</label>
                    <input
                        type="text"
                        placeholder="Search for anything..."
                        v-model="searchParam"
                    />
                </div>
                <div>
                    <label>Filter by Status</label>
                    <select name="status" id="status" v-model="searchStatus">
                        <option value=null selected disabled hidden>
                            —
                        </option>
                        <option value="inStash">In Stash</option>
                        <option value="inUse">In Use</option>
                        <option value="usedUp">Used Up</option>
                        <option value="traded">Traded</option>
                        <option value="gifted">Gifted</option>
                    </select>
                </div>
                <div>
                    <label>Filter by Type</label>
                    <select name="type" id="type" v-model="searchType">
                        <option value=null selected disabled hidden>
                            —
                        </option>
                        <option value="fiber">Fiber</option>
                        <option value="yarn">Yarn</option>
                    </select>
                </div>
                <!-- IF FIBER OR YARN -->
                <div
                    v-if="
                        this.searchType == 'fiber' || this.searchType == 'yarn'
                    "
                >
                    <label>Search for Any:</label>
                    <div class="color-options">
                        <button
                            v-bind:class="{ selected: searchRed }"
                            @click.prevent="this.searchRed = !this.searchRed"
                        >
                            Red
                        </button>
                        <button
                            v-bind:class="{ selected: searchRedOrange }"
                            @click.prevent="
                                this.searchRedOrange = !this.searchRedOrange
                            "
                        >
                            Red-orange
                        </button>
                        <button
                            v-bind:class="{ selected: searchOrange }"
                            @click.prevent="
                                this.searchOrange = !this.searchOrange
                            "
                        >
                            Orange
                        </button>
                        <button
                            v-bind:class="{ selected: searchOrangeYellow }"
                            @click.prevent="
                                this.searchOrangeYellow =
                                    !this.searchOrangeYellow
                            "
                        >
                            Orange-yellow
                        </button>
                        <button
                            v-bind:class="{ selected: searchYellow }"
                            @click.prevent="
                                this.searchYellow = !this.searchYellow
                            "
                        >
                            Yellow
                        </button>
                        <button
                            v-bind:class="{ selected: searchYellowGreen }"
                            @click.prevent="
                                this.searchYellowGreen = !this.searchYellowGreen
                            "
                        >
                            Yellow-green
                        </button>
                        <button
                            v-bind:class="{ selected: searchGreen }"
                            @click.prevent="
                                this.searchGreen = !this.searchGreen
                            "
                        >
                            Green
                        </button>
                        <button
                            v-bind:class="{ selected: searchBlueGreen }"
                            @click.prevent="
                                this.searchBlueGreen = !this.searchBlueGreen
                            "
                        >
                            Blue-green
                        </button>
                        <button
                            v-bind:class="{ selected: searchBlue }"
                            @click.prevent="this.searchBlue = !this.searchBlue"
                        >
                            Blue
                        </button>
                        <button
                            v-bind:class="{ selected: searchBluePurple }"
                            @click.prevent="
                                this.searchBluePurple = !this.searchBluePurple
                            "
                        >
                            Blue-purple
                        </button>
                        <button
                            v-bind:class="{ selected: searchPurple }"
                            @click.prevent="
                                this.searchPurple = !this.searchPurple
                            "
                        >
                            Purple
                        </button>
                        <button
                            v-bind:class="{ selected: searchPink }"
                            @click.prevent="this.searchPink = !this.searchPink"
                        >
                            Pink
                        </button>
                        <button
                            v-bind:class="{ selected: searchWhite }"
                            @click.prevent="
                                this.searchWhite = !this.searchWhite
                            "
                        >
                            White
                        </button>
                        <button
                            v-bind:class="{ selected: searchGray }"
                            @click.prevent="this.searchGray = !this.searchGray"
                        >
                            Gray
                        </button>
                        <button
                            v-bind:class="{ selected: searchBlack }"
                            @click.prevent="
                                this.searchBlack = !this.searchBlack
                            "
                        >
                            Black
                        </button>
                        <button
                            v-bind:class="{ selected: searchCream }"
                            @click.prevent="
                                this.searchCream = !this.searchCream
                            "
                        >
                            Cream / Natural
                        </button>
                        <button
                            v-bind:class="{ selected: searchBrown }"
                            @click.prevent="
                                this.searchBrown = !this.searchBrown
                            "
                        >
                            Brown
                        </button>
                        <button
                            v-bind:class="{ selected: searchRainbow }"
                            @click.prevent="
                                this.searchRainbow = !this.searchRainbow
                            "
                        >
                            Rainbow
                        </button>
                    </div>
                </div>
                <!-- IF FIBER TYPE -->
                <div v-if="this.searchType == 'fiber'">
                    <label>Filter by Minimum Fiber Quantity</label>
                    <div class="input-select">
                        <input
                            type="text"
                            class="input-select-input"
                            v-model="searchFiberQuantity"
                            placeholder="0"
                        />
                        <select
                            name="fiberUnit"
                            id="fiberUnit"
                            v-model="searchFiberUnit"
                        >
                            <option value="oz">oz</option>
                            <option value="g">grams</option>
                        </select>
                    </div>
                </div>
                <!-- IF YARN TYPE -->
                <div v-if="this.searchType == 'yarn'">
                    <label>Filter by Yarn Weight</label>
                    <select
                        name="yarnWeight"
                        id="yarnWeight"
                        v-model="searchYarnWeight"
                    >
                        <option value=null selected disabled hidden>
                            —
                        </option>
                        <option value="lace">Lace</option>
                        <option value="lfingering">Light Fingering</option>
                        <option value="fingering">Fingering</option>
                        <option value="sport">Sport</option>
                        <option value="dk">DK</option>
                        <option value="worsted">Worsted</option>
                        <option value="aran">Aran</option>
                        <option value="bulky">Bulky</option>
                        <option value="sbulky">Super Bulky</option>
                    </select>
                </div>
                <div v-if="this.searchType == 'yarn'">
                    <label>Filter by Minimum Yarn Quantity</label>
                    <div class="input-select">
                        <input
                            type="text"
                            class="input-select-input"
                            v-model="searchYarnQuantity"
                            placeholder="0"
                        />
                        <select
                            name="fiberUnit"
                            id="fiberUnit"
                            v-model="searchYarnUnit"
                        >
                            <option value="yd">yards</option>
                            <option value="m">meters</option>
                        </select>
                    </div>
                </div>
                <div>
                    <button id="submit-search">Search!</button>
                    <p id="reset-search" @click="reset">Reset Stash Search</p>
                </div>
            </form>
        </div>
        <div class="stash-body">
            <div class="stash-header">
                <h2>{{ $store.state.selectedUser?.username }}'s Stash</h2>
                <h4
                    @click="createStash"
                    v-if="$store.state.sessionUser?.id == $route.params.id"
                >
                    <i class="fas fa-plus-circle" />Add to Stash
                </h4>
            </div>
            <div class="stash-gallery" v-if="$store.state.usersStash?.length">
                <div
                    class="stash-card"
                    v-for="stashItem in $store.state.usersStash"
                    :key="stashItem.id"
                >
                    <img
                        v-if="stashItem.stashItemImages.length"
                        @click="redirectDetail(stashItem.id)"
                        class="card-image"
                        :src="stashItem.stashItemImages[0].imageURL"
                        alt="User uploaded image of stash item"
                    />
                    <img
                        v-else
                        @click="redirectDetail(stashItem.id)"
                        class="card-image"
                        src="https://knotelry.s3.amazonaws.com/image-placeholder.png"
                        alt="No image found"
                    />
                    <p
                        @click="redirectDetail(stashItem.id)"
                        class="card-header"
                    >
                        {{ stashItem.title }}
                    </p>
                </div>
            </div>
            <div class="stash-gallery-no-results" v-else>
                <h4>No results!</h4>
                <p>
                    Maybe try broadening your search or
                    <span id="create-link" @click="createStash"
                        >adding to your stash?</span
                    >
                </p>
            </div>
        </div>
    </div>
</template>

<script>
import { mapMutations } from "vuex";

export default {
    name: "Stash",
    mounted() {
        this.$store.commit("clearSelectedUser");
        const data = loadUser(this.$route.params.id).then((data) => {
            if (data) {
                this.$store.commit("setSelectedUser", data);
            } else {
                this.$router.push("/404");
            }
        });
        const stashData = loadUsersStash(this.$route.params.id).then(
            (stashData) => {
                if (stashData) {
                    this.$store.commit("setUsersStash", stashData);
                }
            }
        );
    },
    data() {
        return {
            searchParam: "",
            searchType: null,
            searchStatus: null,
            searchFiberQuantity: null,
            searchFiberUnit: "oz",
            searchYarnWeight: null,
            searchYarnQuantity: null,
            searchYarnUnit: "yd",

            searchRed: false,
            searchRedOrange: false,
            searchOrange: false,
            searchOrangeYellow: false,
            searchYellow: false,
            searchYellowGreen: false,
            searchGreen: false,
            searchBlueGreen: false,
            searchBlue: false,
            searchBluePurple: false,
            searchPurple: false,
            searchPink: false,
            searchWhite: false,
            searchGray: false,
            searchBlack: false,
            searchCream: false,
            searchBrown: false,
            searchRainbow: false,
        };
    },
    methods: {
        redirectDetail(id) {
            this.$router.push(`/stash/${id}`);
        },
        reset() {
            this.searchParam = "";
            this.searchType = null;
            this.searchStatus = null;
            this.searchFiberQuantity = null;
            this.searchFiberUnit = "oz";
            this.searchYarnQuantity = null;
            this.searchYarnUnit = "yd";

            let stashData = loadUsersStash(this.$route.params.id).then(
                (stashData) => {
                    if (stashData) {
                        this.$store.commit("setUsersStash", stashData);
                    }
                }
            );
        },
        submit() {
            let stashData = loadUsersStash(this.$route.params.id).then(
                (stashData) => {
                    if (stashData) {
                        stashData = stashData.stash;
                    }
                    if (this.searchParam) {
                        const temp = [];
                        stashData.forEach((stashItem) => {
                            if (
                                stashItem.title
                                    ?.toLowerCase()
                                    .includes(this.searchParam.toLowerCase()) ||
                                stashItem.description
                                    ?.toLowerCase()
                                    .includes(this.searchParam.toLowerCase())
                            ) {
                                temp.push(stashItem);
                            }
                        });
                        stashData = temp;
                    }
                    if (this.searchType) {
                        const temp = [];
                        stashData.forEach((stashItem) => {
                            if (stashItem.type == this.searchType) {
                                temp.push(stashItem);
                            }
                        });
                        stashData = temp;
                    }
                    if (this.searchStatus) {
                        const temp = [];
                        stashData.forEach((stashItem) => {
                            if (stashItem.status == this.searchStatus) {
                                temp.push(stashItem);
                            }
                        });
                        stashData = temp;
                    }
                    if (this.searchFiberQuantity) {
                        const temp = [];
                        if (this.searchFiberUnit == "oz") {
                            stashData.forEach((stashItem) => {
                                if (
                                    stashItem.fiberQuantityUnit == "oz" &&
                                    stashItem.fiberQuantity >=
                                        this.searchFiberQuantity
                                ) {
                                    temp.push(stashItem);
                                } else if (
                                    stashItem.fiberQuantityUnit == "g" &&
                                    stashItem.fiberQuantity / 28.35 >=
                                        this.searchFiberQuantity
                                ) {
                                    temp.push(stashItem);
                                }
                            });
                            stashData = temp;
                        } else if (this.searchFiberUnit == "g") {
                            stashData.forEach((stashItem) => {
                                if (
                                    stashItem.fiberQuantityUnit == "oz" &&
                                    stashItem.fiberQuantity * 28.35 >=
                                        this.searchFiberQuantity
                                ) {
                                    temp.push(stashItem);
                                } else if (
                                    stashItem.fiberQuantityUnit == "g" &&
                                    stashItem.fiberQuantity >=
                                        this.searchFiberQuantity
                                ) {
                                    temp.push(stashItem);
                                }
                                stashData = temp;
                            });
                        }
                    }
                    if (this.searchYarnWeight) {
                        const temp = [];
                        stashData.forEach((stashItem) => {
                            if (stashItem.yarnWeight == this.searchYarnWeight) {
                                temp.push(stashItem);
                            }
                        });
                        stashData = temp;
                    }
                    if (this.searchYarnQuantity) {
                        const temp = [];
                        if (this.searchYarnUnit == "yd") {
                            stashData.forEach((stashItem) => {
                                if (
                                    stashItem.lengthUnit == "yd" &&
                                    stashItem.lengthStashed >=
                                        this.searchYarnQuantity
                                ) {
                                    temp.push(stashItem);
                                } else if (
                                    stashItem.lengthUnit == "m" &&
                                    stashItem.lengthStashed * 1.094 >=
                                        this.searchYarnQuantity
                                ) {
                                    temp.push(stashItem);
                                }
                            });
                            stashData = temp;
                        } else if ((this.searchYarnUnit = "m")) {
                            stashData.forEach((stashItem) => {
                                if (
                                    stashItem.lengthUnit == "yd" &&
                                    stashItem.lengthStashed / 1.094 >=
                                        this.searchYarnQuantity
                                ) {
                                    temp.push(stashItem);
                                } else if (
                                    stashItem.lengthUnit == "m" &&
                                    stashItem.lengthStashed >=
                                        this.searchYarnQuantity
                                ) {
                                    temp.push(stashItem);
                                }
                            });
                            stashData = temp;
                        }
                    }

                    if (
                        this.searchRed ||
                        this.searchRedOrange ||
                        this.searchOrange ||
                        this.searchOrangeYellow ||
                        this.searchYellow ||
                        this.searchYellowGreen ||
                        this.searchGreen ||
                        this.searchBlueGreen ||
                        this.searchBlue ||
                        this.searchBluePurple ||
                        this.searchPurple ||
                        this.searchPink ||
                        this.searchWhite ||
                        this.searchGray ||
                        this.searchBlack ||
                        this.searchCream ||
                        this.searchBrown ||
                        this.searchRainbow
                    ) {
                        const temp = new Set();
                        stashData.forEach((stashItem) => {
                            const colorsArr = stashItem.colors?.split(" ");
                            if (this.searchRed && colorsArr.includes("red"))
                                temp.add(stashItem);
                            if (
                                this.searchRedOrange &&
                                colorsArr.includes("redorange")
                            )
                                temp.add(stashItem);
                            if (
                                this.searchOrange &&
                                colorsArr.includes("orange")
                            )
                                temp.add(stashItem);
                            if (
                                this.searchOrangeYellow &&
                                colorsArr.includes("orangeyellow")
                            )
                                temp.add(stashItem);
                            if (
                                this.searchYellow &&
                                colorsArr.includes("yellow")
                            )
                                temp.add(stashItem);
                            if (
                                this.searchYellowGreen &&
                                colorsArr.includes("yellowgreen")
                            )
                                temp.add(stashItem);
                            if (this.searchGreen && colorsArr.includes("green"))
                                temp.add(stashItem);
                            if (
                                this.searchBlueGreen &&
                                colorsArr.includes("bluegreen")
                            )
                                temp.add(stashItem);
                            if (this.searchBlue && colorsArr.includes("blue"))
                                temp.add(stashItem);
                            if (
                                this.searchBluePurple &&
                                colorsArr.includes("bluepurple")
                            )
                                temp.add(stashItem);
                            if (
                                this.searchPurple &&
                                colorsArr.includes("purple")
                            )
                                temp.add(stashItem);
                            if (this.searchPink && colorsArr.includes("pink"))
                                temp.add(stashItem);
                            if (this.searchWhite && colorsArr.includes("white"))
                                temp.add(stashItem);
                            if (this.searchGray && colorsArr.includes("gray"))
                                temp.add(stashItem);
                            if (this.searchBlack && colorsArr.includes("black"))
                                temp.add(stashItem);
                            if (this.searchCream && colorsArr.includes("cream"))
                                temp.add(stashItem);
                            if (this.searchBrown && colorsArr.includes("brown"))
                                temp.add(stashItem);
                            if (
                                this.searchRainbow &&
                                colorsArr.includes("rainbow")
                            )
                                temp.add(stashItem);
                        });
                        stashData = Array.from(temp);
                    }

                    this.$store.commit("setUsersStash", stashData);
                    window.scrollTo(0, 0);
                }
            );
        },
        createStash: function () {
            this.$router.push(`/stash/create`);
        },
    },
    mutations: {
        ...mapMutations,
    },
};

const loadUser = async (userId) => {
    const response = await fetch(`/api/users/${userId}`);
    if (response.ok) {
        const data = await response.json();
        return data;
    } else {
        const data = false;
        return false;
    }
};

const loadUsersStash = async (userId) => {
    const response = await fetch(`/api/stash/users/${userId}`);
    if (response.ok) {
        const stashData = await response.json();
        return stashData;
    } else {
        return stashData;
    }
};
</script>

<style scoped>
.stash-page {
    display: grid;
    grid-template-columns: 300px 1fr;
    column-gap: 4%;
}

.stash-page-left {
    min-height: calc(100vh - 70px);
    height: 100%;
    margin-bottom: 40px;
}

.stash-search-container {
    border: 1px solid var(--color-shadow);
    border-radius: 4px;
    box-shadow: 2px 2px 2px var(--color-shadow);
    margin-top: 120px;
    margin-left: 32px;
    margin-bottom: 40px;
    position: sticky;
    top: 32px;
}

.stash-search-container > .header {
    width: 100%;
    background-color: var(--color-primary-contrast);
    margin: 0px;
    padding-top: 8px;
    padding-bottom: 8px;
    color: white;
    letter-spacing: 1px;
}

.stash-search-container > div {
    margin-top: 12px;
    margin-bottom: 12px;
    display: flex;
    flex-direction: column;
}

.stash-search-container > div > label {
    font-size: 15px;
}

.input-select {
    display: grid;
    grid-template-columns: 130px 135px;
}

.input-select-input {
    margin-left: 20px;
    margin-right: -10px;
}

input {
    font-size: 14px;
    font-family: "Open Sans", sans-serif;
    border-radius: 6px;
    border: 1px solid var(--color-shadow);
    padding-top: 6px;
    padding-bottom: 6px;
    padding-left: 10px;
    padding-right: 10px;
    margin-top: 8px;
    margin-bottom: 8px;
    margin-right: 20px;
    margin-left: 20px;
}

select {
    font-size: 14px;
    font-family: "Open Sans", sans-serif;
    border-radius: 6px;
    border: 1px solid var(--color-shadow);
    padding-top: 6px;
    padding-bottom: 6px;
    padding-left: 10px;
    padding-right: 10px;
    margin-top: 8px;
    margin-bottom: 8px;
    margin-right: 20px;
    margin-left: 20px;
}

button {
    border: 1px solid var(--color-shadow);
    background-color: white;
    border-radius: 4px;
    color: var(--color-shadow);
    box-shadow: 1px 1px 1px var(--color-shadow);
    padding-top: 4px;
    padding-bottom: 4px;
    font-family: "Open Sans", sans-serif;
    letter-spacing: 1px;
    margin-right: 20px;
    margin-left: 20px;
    margin-top: 4px;
    margin-bottom: 4px;
}

button:hover {
    cursor: pointer;
}

button:active {
    box-shadow: 2px 2px 2px var(--color-shadow);
}

.color-options {
    display: grid;
    grid-template-columns: repeat(auto-fill, 124px);
    justify-content: space-between;
    row-gap: 2px;
    padding-left: 8px;
    padding-right: 8px;
    padding-top: 4px;
}

.color-options > button {
    font-size: 12px;
    letter-spacing: 0px;
    margin: 2px;
}

.selected {
    background-color: var(--color-primary-contrast);
    color: white;
}

#submit-search {
    background-color: var(--color-primary-contrast);
    color: white;
    font-size: 16px;
}

#reset-search {
    border: 1px solid var(--color-shadow);
    background-color: white;
    border-radius: 4px;
    color: var(--color-shadow);
    box-shadow: 1px 1px 1px var(--color-shadow);
    padding-top: 4px;
    padding-bottom: 4px;
    font-family: "Open Sans", sans-serif;
    letter-spacing: 1px;
    margin-right: 20px;
    margin-left: 20px;
    margin-top: 4px;
    margin-bottom: 4px;
    font-size: 14px;
}

#reset-search:hover {
    cursor: pointer;
}

#reset-search:active {
    box-shadow: 2px 2px 2px var(--color-shadow);
}

.stash-body {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    text-align: left;
    padding-top: 40px;
    padding-bottom: 32px;
    padding-right: 8%;
    overflow: auto;
}

.stash-header {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
}

.stash-header > h4 {
    display: flex;
    flex-direction: row;
    column-gap: 8px;
    align-items: center;
    background-color: var(--color-primary-contrast);
    color: white;
    padding-left: 12px;
    padding-right: 12px;
    padding-top: 6px;
    padding-bottom: 6px;
    border-radius: 16px;
    border: 1px solid var(--color-shadow);
    box-shadow: 2px 2px 2px var(--color-shadow);
    font-weight: normal;
}

.stash-header > h4:hover {
    cursor: pointer;
}

.stash-header > h4:active {
    box-shadow: 3px 3px 2px var(--color-shadow);
}

.stash-gallery {
    display: grid;
    grid-template-columns: repeat(auto-fill, 160px);
    grid-gap: 12px;
    justify-content: space-between;
}

.stash-gallery-no-results {
    display: flex;
    flex-direction: column;
}

.stash-card {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 160px;
    margin: 0px;
    margin: 8px;
}

.stash-card > p {
    margin: 8px;
    font-size: 14px;
    text-align: center;
}

.card-image {
    width: 160px;
    height: 160px;
    object-fit: cover;
    border: 1px solid var(--color-shadow);
    border-radius: 4px;
}

.card-image:hover {
    cursor: pointer;
}

.card-header:hover {
    cursor: pointer;
    font-weight: bold;
}

#create-link {
    font-weight: bold;
}

#create-link:hover {
    cursor: pointer;
}
</style>
