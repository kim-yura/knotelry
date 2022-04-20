<template>
    <div class="stash-detail">
        <div class="left">
            <span v-if="this.images">
                <img
                    v-for="image in this.images"
                    :key="image.id"
                    class="detail-image"
                    :src="image.imageURL"
                    alt="User-uploaded image of stash item"
                />
            </span>
            <img
                v-else
                class="detail-image"
                src="https://knotelry.s3.amazonaws.com/image-placeholder.png"
                alt="No image found"
            />
            <div class="stash-header">
                <h2>{{ this.title }}</h2>
            </div>
            <div
                v-if="$store.state.sessionUser?.id == this.user?.id"
                class="stash-options"
            >
                <button @click="editStash">Edit</button>
                <button @click="deleteStash">Delete</button>
            </div>
        </div>
        <div class="right">
            <!-- METADATA -->
            <div class="detail-text">
                <div class="text-label">Type:</div>
                <div class="text-content" v-if="this.type == 'fiber'">
                    Fiber
                </div>
                <div class="text-content" v-else-if="this.type == 'yarn'">
                    Yarn
                </div>
                <div class="text-content" v-else>—</div>
            </div>
            <div class="detail-text">
                <div class="text-label">Description:</div>
                <div class="text-content" v-if="this.description">
                    {{ this.description }}
                </div>
                <div class="text-content" v-else>—</div>
            </div>
            <div class="detail-text">
                <div class="text-label">Status:</div>
                <div class="text-content" v-if="this.status == 'inUse'">
                    In Use
                </div>
                <div class="text-content" v-else-if="this.status == 'inStash'">
                    In Stash
                </div>
                <div class="text-content" v-else-if="this.status == 'usedUp'">
                    Used Up
                </div>
                <div class="text-content" v-else-if="this.status == 'traded'">
                    Traded
                </div>
                <div class="text-content" v-else-if="this.status == 'gifted'">
                    Gifted
                </div>
                <div class="text-content" v-else-if="this.status == 'sold'">
                    Sold
                </div>
                <div class="text-content" v-else>—</div>
            </div>
            <div class="detail-text">
                <div class="text-label">Date Acquired:</div>
                <div class="text-content" v-if="this.acquired">
                    {{ this.acquired.slice(5, 16) }}
                </div>
                <div class="text-content" v-else>—</div>
            </div>
            <div class="detail-text">
                <div class="text-label">Acquired From:</div>
                <div class="text-content" v-if="this.acquiredFrom">
                    {{ this.acquiredFrom }}
                </div>
                <div class="text-content" v-else>—</div>
            </div>
            <div class="detail-text">
                <div class="text-label">Purchase Price:</div>
                <div class="text-content" v-if="this.acquiredPrice">
                    {{ this.acquiredPrice }} {{ this.acquiredCurrency }}
                </div>
                <div class="text-content" v-else>—</div>
            </div>
            <div class="divider" />
            <!-- DYER NAME AND COLORWAY -->
            <div
                v-if="this.type == 'fiber' || this.type == 'yarn'"
                class="detail-text"
            >
                <div class="text-label">Dyer Name:</div>
                <div class="text-content" v-if="this.dyerName">
                    {{ this.dyerName }}
                </div>
                <div class="text-content" v-else>—</div>
            </div>
            <div
                v-if="this.type == 'fiber' || this.type == 'yarn'"
                class="detail-text"
            >
                <div class="text-label">Colorway Name:</div>
                <div class="text-content" v-if="this.colorwayName">
                    {{ this.colorwayName }}
                </div>
                <div class="text-content" v-else>—</div>
            </div>
            <!-- FIBER DETAILS -->
            <div v-if="this.type == 'fiber'" class="detail-text">
                <div class="text-label">Amount Stashed:</div>
                <div class="text-content" v-if="this.fiberQuantity">
                    {{ this.fiberQuantity.toFixed(2) }} {{ this.fiberQuantityUnit }}
                </div>
                <div class="text-content" v-else>—</div>
            </div>
            <!-- YARN DETAILS -->
            <div v-if="this.type == 'yarn'" class="detail-text">
                <div class="text-label">Yarn Weight:</div>
                <div class="text-content" v-if="this.yarnWeight == 'lace'">
                    Lace Weight
                </div>
                <div
                    class="text-content"
                    v-else-if="this.yarnWeight == 'lfingering'"
                >
                    Light Fingering Weight
                </div>
                <div
                    class="text-content"
                    v-else-if="this.yarnWeight == 'fingering'"
                >
                    Fingering Weight
                </div>
                <div
                    class="text-content"
                    v-else-if="this.yarnWeight == 'sport'"
                >
                    Sport Weight
                </div>
                <div class="text-content" v-else-if="this.yarnWeight == 'dk'">
                    DK Weight
                </div>
                <div
                    class="text-content"
                    v-else-if="this.yarnWeight == 'worsted'"
                >
                    Worsted Weight
                </div>
                <div class="text-content" v-else-if="this.yarnWeight == 'aran'">
                    Aran Weight
                </div>
                <div
                    class="text-content"
                    v-else-if="this.yarnWeight == 'bulky'"
                >
                    Bulky Weight
                </div>
                <div
                    class="text-content"
                    v-else-if="this.yarnWeight == 'sbulky'"
                >
                    Super Bulky Weight
                </div>
                <div class="text-content" v-else>—</div>
            </div>
            <div v-if="this.type == 'yarn'" class="detail-text">
                <div class="text-label">Skein Details:</div>
                <div
                    class="text-content"
                    v-if="this.lengthPerSkein && this.weightPerSkein"
                >
                    {{ this.lengthPerSkein }} {{ this.lengthUnit }} /
                    {{ this.weightPerSkein }} {{ this.weightUnit }}
                </div>
                <div class="text-content" v-else-if="this.lengthPerSkein">
                    {{ this.lengthPerSkein }} {{ this.lengthUnit }}
                </div>
                <div class="text-content" v-else-if="this.weightPerSkein">
                    {{ this.weightPerSkein }} {{ this.weightUnit }}
                </div>
                <div class="text-content" v-else>—</div>
            </div>
            <div v-if="this.type == 'yarn'" class="detail-text">
                <div class="text-label">Amount Stashed:</div>
                <div class="stashed-content">
                    <p v-if="this.skeinsStashed">
                        {{ this.skeinsStashed.toFixed(2) }} skeins
                    </p>
                    <p v-else-if="this.lengthStashed && this.lengthPerSkein">
                        {{
                            (this.lengthStashed / this.lengthPerSkein).toFixed(
                                2
                            )
                        }}
                        skeins
                    </p>
                    <p v-else-if="this.weightStashed && this.weightPerSkein">
                        {{
                            (this.weightStashed / this.weightPerSkein).toFixed(
                                2
                            )
                        }}
                        skeins
                    </p>
                    <p v-else>— skeins</p>
                    <p v-if="this.lengthStashed">
                        {{ this.lengthStashed.toFixed(2) }}
                        {{ this.lengthUnit }}
                    </p>
                    <p v-else-if="this.skeinsStashed && this.lengthPerSkein">
                        {{
                            (this.skeinsStashed * this.lengthPerSkein).toFixed(
                                2
                            )
                        }}
                        {{ this.lengthUnit }}
                    </p>
                    <p
                        v-else-if="
                            this.weightStashed &&
                            this.weightPerSkein &&
                            this.lengthPerSkein
                        "
                    >
                        {{
                            (
                                (this.weightStashed / this.weightPerSkein) *
                                this.lengthPerSkein
                            ).toFixed(2)
                        }}
                        {{ this.lengthUnit }}
                    </p>
                    <p v-else>— {{ this.lengthUnit }}</p>
                    <p v-if="this.weightStashed">
                        {{ this.weightStashed.toFixed(2) }}
                        {{ this.weightUnit }}
                    </p>
                    <p v-else-if="this.skeinsStashed && this.weightPerSkein">
                        {{
                            (this.weightPerSkein * this.skeinsStashed).toFixed(
                                2
                            )
                        }}
                        {{ this.weightUnit }}
                    </p>
                    <p
                        v-else-if="
                            this.lengthStashed &&
                            this.lengthPerSkein &&
                            this.weightPerSkein
                        "
                    >
                        {{
                            (
                                (this.lengthStashed / this.lengthPerSkein) *
                                this.weightPerSkein
                            ).toFixed(2)
                        }}
                        {{ this.weightUnit }}
                    </p>
                    <p v-else>— {{ this.weightUnit }}</p>
                </div>
            </div>
            <div class="detail-text">
                <div class="text-label">Amount Remaining:</div>
                <!-- Render for yarn remainder -->
                <div class="stashed-content" v-if="this.type == 'yarn'">
                    <p v-if="isNaN(this.skeinsRemaining)">— skeins</p>
                    <p v-else>{{ this.skeinsRemaining.toFixed(2) }} skeins</p>
                    <p v-if="isNaN(this.lengthRemaining)">
                        — {{ this.lengthUnit }}
                    </p>
                    <p v-else>
                        {{ this.lengthRemaining.toFixed(2) }}
                        {{ this.lengthUnit }}
                    </p>
                    <p v-if="isNaN(this.weightRemaining)">
                        — {{ this.weightUnit }}
                    </p>
                    <p v-else>
                        {{ this.weightRemaining.toFixed(2) }}
                        {{ this.weightUnit }}
                    </p>
                </div>
                <!-- Render for fiber remainder -->
                <div class="stashed-content" v-if="this.type == 'fiber'">
                    <p v-if="isNaN(this.fiberQuantityRemaining)">
                        — {{ this.fiberQuantityUnit }}
                    </p>
                    <p v-else>
                        {{ this.fiberQuantityRemaining.toFixed(2) }}
                        {{ this.fiberQuantityUnit }}
                    </p>
                </div>
            </div>
            <div
                v-if="this.type == 'yarn' || this.type == 'fiber'"
                class="detail-text"
            >
                <div class="text-label">Colors:</div>
                <div class="colors-container">
                    <p class="color-container" v-if="this.isRed">Red</p>
                    <p class="color-container" v-if="this.isRedOrange">
                        Red-orange
                    </p>
                    <p class="color-container" v-if="this.isOrange">Orange</p>
                    <p class="color-container" v-if="this.isOrangeYellow">
                        Orange-yellow
                    </p>
                    <p class="color-container" v-if="this.isYellow">Yellow</p>
                    <p class="color-container" v-if="this.isYellowGreen">
                        Yellow-green
                    </p>
                    <p class="color-container" v-if="this.isGreen">Green</p>
                    <p class="color-container" v-if="this.isBlueGreen">
                        Blue-green
                    </p>
                    <p class="color-container" v-if="this.isBlue">Blue</p>
                    <p class="color-container" v-if="this.isBluePurple">
                        Blue-purple
                    </p>
                    <p class="color-container" v-if="this.isPurple">Purple</p>
                    <p class="color-container" v-if="this.isPink">Pink</p>
                    <p class="color-container" v-if="this.isWhite">White</p>
                    <p class="color-container" v-if="this.isGray">Gray</p>
                    <p class="color-container" v-if="this.isBlack">Black</p>
                    <p class="color-container" v-if="this.isCream">Cream</p>
                    <p class="color-container" v-if="this.isBrown">Brown</p>
                    <p class="color-container" v-if="this.isRainbow">Rainbow</p>
                </div>
            </div>
            <div
                v-if="this.type == 'fiber' || this.type == 'yarn'"
                class="divider"
            />
            <!-- NOTES -->
            <div class="detail-text">
                <div class="text-label">Notes:</div>
                <div class="text-content" v-if="this.notes">
                    {{ this.notes }}
                </div>
                <div class="text-content" v-else>—</div>
            </div>
            <div class="divider" />
            <!-- PROJECTS GO HERE -->
            <div class="detail-text">
                <div class="text-label">Linked Projects:</div>
                <div
                    class="linked-project-gallery"
                    v-if="this.linkedProjects?.length"
                >
                    <div
                        class="project"
                        v-for="project in linkedProjects"
                        :key="project.id"
                    >
                        <img
                            class="project-image"
                            v-if="project.projectImages.length"
                            :src="project.projectImages[0].imageURL"
                            alt="User-uploaded image of project"
                            @click.prevent="redirectProject(project.id)"
                        />
                        <img
                            class="project-image"
                            v-else
                            src="https://knotelry.s3.amazonaws.com/image-placeholder.png"
                            alt="No image found"
                            @click.prevent="redirectProject(project.id)"
                        />
                        <p
                            class="project-link"
                            @click.prevent="redirectProject(project.id)"
                        >
                            {{ project.title }}
                        </p>
                    </div>
                </div>
                <div class="text-content" v-else>No linked projects</div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "StashDetail",
    mounted() {
        const data = loadStashItem(parseInt(this.$route.params.stashId)).then(
            (data) => {
                if (data) {
                    this.title = data.title;
                    this.description = data.description;
                    this.type = data.type;
                    this.status = data.status;

                    this.acquired = data.acquired;
                    this.acquiredFrom = data.acquiredFrom;
                    this.acquiredPrice = data.acquiredPrice;
                    this.acquiredCurrency = data.acquiredCurrency;

                    if (data.colors?.length) {
                        const colorsArr = data.colors.split(" ");
                        if (colorsArr.includes("red")) this.isRed = true;
                        if (colorsArr.includes("redorange"))
                            this.isRedOrange = true;
                        if (colorsArr.includes("orange")) this.isOrange = true;
                        if (colorsArr.includes("orangeyellow"))
                            this.isOrangeYellow = true;
                        if (colorsArr.includes("yellow")) this.isYellow = true;
                        if (colorsArr.includes("yellowgreen"))
                            this.isYellowGreen = true;
                        if (colorsArr.includes("green")) this.isGreen = true;
                        if (colorsArr.includes("bluegreen"))
                            this.isBlueGreen = true;
                        if (colorsArr.includes("blue")) this.isBlue = true;
                        if (colorsArr.includes("bluepurple"))
                            this.isBluePurple = true;
                        if (colorsArr.includes("purple")) this.isPurple = true;
                        if (colorsArr.includes("pink")) this.isPink = true;
                        if (colorsArr.includes("white")) this.isWhite = true;
                        if (colorsArr.includes("gray")) this.isGray = true;
                        if (colorsArr.includes("black")) this.isBlack = true;
                        if (colorsArr.includes("cream")) this.isCream = true;
                        if (colorsArr.includes("brown")) this.isBrown = true;
                        if (colorsArr.includes("rainbow"))
                            this.isRainbow = true;
                    }

                    this.dyerName = data.dyerName;
                    this.colorwayName = data.colorwayName;

                    this.fiberContent = data.fiberContent;
                    this.fiberQuantity = data.fiberQuantity;
                    this.fiberQuantityUnit = data.fiberQuantityUnit;

                    this.yarnWeight = data.yarnWeight;
                    this.lengthPerSkein = data.lengthPerSkein;
                    this.lengthUnit = data.lengthUnit;
                    this.weightPerSkein = data.weightPerSkein;
                    this.weightUnit = data.weightUnit;
                    this.skeinsStashed = data.skeinsStashed;
                    this.lengthStashed = data.lengthStashed;
                    this.weightStashed = data.weightStashed;
                    this.isHandspun = data.isHandspun;

                    this.notes = data.notes;
                    this.images = data.stashItemImages;

                    this.skeinsRemaining = this.skeinsStashed;
                    this.lengthRemaining = this.lengthStashed;
                    this.weightRemaining = this.weightStashed;

                    this.user = data.user;
                } else {
                    this.$router.push("/404");
                }
                const projectsData = loadLinkedProjects(
                    parseInt(this.$route.params.stashId)
                ).then((projectsData) => {
                    if (projectsData) {
                        this.linkedProjects = Object.values(projectsData)[0];
                    }
                });
                const materialsData = loadLinkedProjectMaterials(
                    parseInt(this.$route.params.stashId)
                ).then((materialsData) => {
                    if (materialsData) {
                        this.linkedProjectMaterials =
                            Object.values(materialsData)[0];

                        // Calculates remainders for yarn
                        if (this.type == "yarn") {
                            let lengthUsed = 0;
                            let weightUsed = 0;
                            let skeinsUsed = 0;

                            this.linkedProjectMaterials.forEach((material) => {
                                if (
                                    material.lengthUsed &&
                                    material.lengthUnit == this.lengthUnit
                                ) {
                                    lengthUsed =
                                        lengthUsed + material.lengthUsed;
                                } else if (
                                    material.lengthUsed &&
                                    material.lengthUnit == "yd" &&
                                    this.lengthUnit == "m"
                                ) {
                                    lengthUsed =
                                        lengthUsed +
                                        material.lengthUsed / 1.094;
                                } else if (
                                    material.lengthUsed &&
                                    material.lengthUnit == "m" &&
                                    this.lengthUnit == "yd"
                                ) {
                                    lengthUsed =
                                        lengthUsed +
                                        material.lengthUsed * 1.094;
                                } else if (
                                    !material.lengthUsed &&
                                    material.weightUsed &&
                                    material.weightUnit == this.weightUnit
                                ) {
                                    weightUsed =
                                        weightUsed + material.weightUsed;
                                } else if (
                                    !material.lengthUsed &&
                                    material.weightUsed &&
                                    material.weightUnit == "g" &&
                                    this.weightUnit == "oz"
                                ) {
                                    weightUsed =
                                        weightUsed +
                                        material.weightUsed / 28.35;
                                } else if (
                                    !material.lengthUsed &&
                                    material.weightUsed &&
                                    material.weightUnit == "oz" &&
                                    this.weightUnit == "g"
                                ) {
                                    weightUsed =
                                        weightUsed +
                                        material.weightUsed * 28.35;
                                } else if (
                                    !material.lengthUsed &&
                                    !material.weightUsed &&
                                    material.skeinsUsed
                                ) {
                                    skeinsUsed =
                                        skeinsUsed + material.skeinsUsed;
                                }
                            });

                            let totalLengthUsed = lengthUsed;
                            if (weightUsed !== 0) {
                                totalLengthUsed =
                                    totalLengthUsed +
                                    (this.lengthPerSkein /
                                        this.weightPerSkein) *
                                        weightUsed;
                            }
                            if (skeinsUsed !== 0) {
                                totalLengthUsed =
                                    totalLengthUsed +
                                    skeinsUsed * this.lengthPerSkein;
                            }

                            this.lengthRemaining =
                                this.lengthStashed - totalLengthUsed;
                            this.weightRemaining =
                                (this.lengthRemaining / this.lengthPerSkein) *
                                this.weightPerSkein;
                            this.skeinsRemaining =
                                this.lengthRemaining / this.lengthPerSkein;
                        }

                        // Calculates remainders for fiber
                        if (this.type == "fiber") {
                            let weightUsed = 0;

                            if (this.linkedProjectMaterials.length) {
                                this.linkedProjectMaterials.forEach(
                                    (material) => {
                                        if (
                                            material.fiberQuantityUsed &&
                                            material.fiberQuantityUnit ==
                                                this.fiberQuantityUnit
                                        ) {
                                            weightUsed =
                                                weightUsed +
                                                material.fiberQuantityUsed;
                                        } else if (
                                            material.fiberQuantityUsed &&
                                            material.fiberQuantityUnit == "g" &&
                                            this.fiberQuantityUnit == "oz"
                                        ) {
                                            weightUsed =
                                                weightUsed +
                                                material.fiberQuantityUsed /
                                                    28.35;
                                        } else if (
                                            material.fiberQuantityUsed &&
                                            material.fiberQuantityUnit ==
                                                "oz" &&
                                            this.fiberQuantityUnit == "g"
                                        ) {
                                            weightUsed =
                                                weightUsed +
                                                material.fiberQuantityUsed *
                                                    28.35;
                                        }

                                        this.fiberQuantityRemaining =
                                            this.fiberQuantity - weightUsed;
                                    }
                                );
                            } else {
                                this.fiberQuantityRemaining = this.fiberQuantity;
                            }
                        }
                    }
                });
            }
        );
    },
    data() {
        return {
            title: null,
            description: null,
            type: null,
            status: null,

            acquired: null,
            acquiredFrom: null,
            acquiredPrice: null,
            acquiredCurrency: null,

            colors: null,

            isRed: false,
            isRedOrange: false,
            isOrange: false,
            isOrangeYellow: false,
            isYellow: false,
            isYellowGreen: false,
            isGreen: false,
            isBlueGreen: false,
            isBlue: false,
            isBluePurple: false,
            isPurple: false,
            isPink: false,
            isWhite: false,
            isGray: false,
            isBlack: false,
            isCream: false,
            isBrown: false,
            isRainbow: false,

            dyerName: null,
            colorwayName: null,

            fiberContent: null,
            fiberQuantity: null,
            fiberQuantityUnit: null,

            yarnWeight: null,
            lengthPerSkein: null,
            lengthUnit: null,
            weightPerSkein: null,
            weightUnit: null,
            skeinsStashed: null,
            lengthStashed: null,
            weightStashed: null,
            isHandspun: false,

            skeinsRemaining: null,
            lengthRemaining: null,
            weightRemaining: null,
            fiberQuantityRemaining: null,

            notes: null,
            images: [],
            user: null,
            linkedProjects: null,
            linkedProjectMaterials: null,
        };
    },
    methods: {
        editStash: function () {
            this.$router.push(`/stash/${this.$route.params.stashId}/edit`);
        },
        deleteStash: function () {
            this.$router.push(`/stash/${this.$route.params.stashId}/delete`);
        },
        redirectProject(id) {
            this.$router.push(`/projects/${id}`);
        },
    },
};

const loadStashItem = async (stashId) => {
    const response = await fetch(`/api/stash/${stashId}`);
    if (response.ok) {
        const data = await response.json();
        return data;
    } else {
        const data = false;
        return false;
    }
};

const loadLinkedProjects = async (stashId) => {
    const response = await fetch(`/api/stash/${stashId}/projects`);
    if (response.ok) {
        const data = await response.json();
        return data;
    } else {
        const data = false;
        return false;
    }
};

const loadLinkedProjectMaterials = async (stashId) => {
    const response = await fetch(`/api/stash/${stashId}/projectmaterials`);
    if (response.ok) {
        const data = await response.json();
        return data;
    } else {
        const data = false;
        return false;
    }
};
</script>

<style scoped>
.stash-detail {
    display: grid;
    grid-template-columns: 400px 1fr;
    padding-left: 14%;
    padding-right: 14%;
    padding-top: 60px;
}

.left {
    display: flex;
    flex-direction: column;
    padding-bottom: 32px;
    padding-right: 8%;
    padding-left: 8%;
}

.detail-image {
    margin-left: auto;
    margin-right: auto;
    height: 300px;
    width: 300px;
    object-fit: cover;
    border: 1px solid var(--color-shadow);
    border-radius: 6px;
}

.stash-header {
    margin-left: auto;
    margin-right: auto;
    width: 300px;
    align-items: center;
    text-align: center;
}

.stash-options {
    margin-left: auto;
    margin-right: auto;
    display: flex;
    flex-direction: row;
    column-gap: 4px;
}

button {
    font-family: "Open Sans", sans-serif;
    letter-spacing: 1px;
    width: 146px;
    padding-top: 4px;
    padding-bottom: 4px;
    border-radius: 4px;
    border: 1px solid var(--color-shadow);
    box-shadow: 1px 1px 1px var(--color-shadow);
    background-color: var(--color-primary-contrast);
    color: white;
    font-size: 16px;
    letter-spacing: 2px;
}

button:hover {
    cursor: pointer;
}

button:active {
    box-shadow: 2px 2px 2px var(--color-shadow);
}

.right {
    display: flex;
    flex-direction: column;
    padding-bottom: 32px;
}

.detail-text {
    display: grid;
    grid-template-columns: 160px 1fr;
    text-align: justify;
    font-size: 14px;
    margin-bottom: 12px;
}

.text-content {
    text-align: left;
}

.stashed-content {
    text-align: left;
    display: flex;
    flex-direction: column;
}

.stashed-content > p {
    margin-top: 0px;
    margin-bottom: 2px;
}

.divider {
    border-top: 1px solid var(--color-shadow);
    margin-top: 10px;
    margin-bottom: 16px;
    padding: 0px;
}

.colors-container {
    display: grid;
    grid-template-columns: repeat(auto-fill, 130px);
    column-gap: 4px;
    row-gap: 4px;
}

.color-container {
    padding-top: 2px;
    padding-bottom: 2px;
    padding-left: 0px;
    padding-right: 0px;
    margin: 0px;
    border: 1px solid var(--color-shadow);
    text-align: center;
    font-size: 13px;
    letter-spacing: 1px;
    border-radius: 4px;
    box-shadow: 1px 1px 2px var(--color-shadow);
}

.linked-project-gallery {
    display: grid;
    grid-template-columns: repeat(auto-fill, 100px);
    grid-gap: 12px;
    justify-content: space-between;
}

.project {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.project-image {
    width: 100px;
    height: 100px;
    object-fit: cover;
    border: 1px solid var(--color-shadow);
    border-radius: 4px;
}

.project-image:hover {
    cursor: pointer;
}

.project-link {
    margin-top: 0px;
    text-align: center;
}

.project-link:hover {
    font-weight: bold;
    cursor: pointer;
}
</style>
