<template>
    <div class="project-form-body">
        <div class="left">
            <div
                class="image-container"
                v-for="image in this.projectImages"
                :key="image.id"
            >
                <img
                    class="project-image"
                    :src="image.imageURL"
                    alt="User uploaded image of project"
                />
                <i
                    class="fas fa-trash-alt"
                    v-if="
                        $store.state.sessionUser?.id ==
                        $store.state.selectedUser?.id
                    "
                    @click="deleteImage($event)"
                    :id="image.id"
                />
            </div>
            <p v-if="!this.projectImages || this.projectImages?.length == 0">
                No linked images
            </p>
            <input
                type="file"
                accept="image/*"
                @change="setImage($event)"
                id="file-input"
            />
            <button
                id="image-upload-button"
                @click="uploadImage($event, this.image)"
            >
                {{ this.imageStatus }}
            </button>
        </div>
        <form class="project-form" @submit.prevent="submit">
            <div class="form-element">
                <div />
                <h2>Editing Project</h2>
            </div>
            <!-- FORM VALIDATION -->
            <div class="form-element" v-if="this.validationErrors.length">
                <div />
                <div class="error-container">
                    <p
                        class="error"
                        v-for="error in this.validationErrors"
                        :key="error"
                    >
                        {{ error }}
                    </p>
                </div>
            </div>
            <!-- METADATA -->
            <div class="form-element">
                <label for="title">Project Title:</label>
                <input
                    type="text"
                    placeholder="Enter a title for your project"
                    v-model="this.title"
                />
            </div>
            <span v-if="this.knitting || this.crocheting || this.sewing">
                <div class="form-element">
                    <label for="pattern">Using Pattern:</label>
                    <div id="pattern-div">
                        <input
                            type="text"
                            placeholder="Pattern title"
                            v-model="this.patternName"
                        />
                        by
                        <input
                            type="text"
                            placeholder="Pattern author"
                            v-model="this.patternAuthor"
                        />
                    </div>
                </div>
                <div class="form-element">
                    <div />
                    <div id="pattern-link">
                        <label for="patternLink">Link to Pattern:</label>
                        <input
                            type="text"
                            placeholder="Enter link to pattern"
                            v-model="this.linkToPattern"
                        />
                    </div>
                </div>
            </span>
            <div class="form-element">
                <label for="description">Description:</label>
                <textarea
                    placeholder="Enter a description for your project"
                    v-model="this.description"
                />
            </div>
            <div class="form-element">
                <label for="status">Status:</label>
                <select v-model="this.status">
                    <option value="null" selected disabled hidden>—</option>
                    <option value="queued">Queued</option>
                    <option value="inProgress">In Progress</option>
                    <option value="finished">Completed</option>
                    <option value="timeout">In Time Out</option>
                </select>
            </div>
            <div class="form-element">
                <label for="taggedCrafts">Craft Types:</label>
                <div class="craft-options">
                    <button
                        v-bind:class="{ selected: spinning }"
                        @click.prevent="this.spinning = !this.spinning"
                    >
                        Spinning
                    </button>
                    <button
                        v-bind:class="{ selected: weaving }"
                        @click.prevent="this.weaving = !this.weaving"
                    >
                        Weaving
                    </button>
                    <button
                        v-bind:class="{ selected: knitting }"
                        @click.prevent="this.knitting = !this.knitting"
                    >
                        Knitting
                    </button>
                    <button
                        v-bind:class="{ selected: crocheting }"
                        @click.prevent="this.crocheting = !this.crocheting"
                    >
                        Crocheting
                    </button>
                    <button
                        v-bind:class="{ selected: sewing }"
                        @click.prevent="this.sewing = !this.sewing"
                    >
                        Sewing
                    </button>
                    <button
                        v-bind:class="{ selected: embroidery }"
                        @click.prevent="this.embroidery = !this.embroidery"
                    >
                        Embroidery
                    </button>
                </div>
            </div>
            <div class="form-element">
                <label for="tags">Tags:</label>
                <input
                    type="text"
                    placeholder="Enter comma-separated tags for your project"
                    v-model="this.tags"
                />
            </div>
            <div class="form-element">
                <label for="attributes">Attributes:</label>
                <input
                    type="text"
                    placeholder="Enter comma-separated attributes for your project"
                    v-model="this.attributes"
                />
            </div>
            <div class="form-element">
                <label for="storedIn">Stored In:</label>
                <input
                    type="text"
                    placeholder="Enter information on where your project is stored"
                    v-model="this.storedIn"
                />
            </div>
            <div class="form-element">
                <label for="projectDates">Project Dates:</label>
                <div id="project-dates-container" class="split-two">
                    <div>
                        <label for="startDate">Start:</label>
                        <input type="date" v-model="this.startDate" />
                    </div>
                    <div>
                        <label for="endDate">End:</label>
                        <input type="date" v-model="this.endDate" />
                    </div>
                </div>
            </div>
            <!-- SPINNING -->
            <span v-if="this.spinning">
                <div class="divider" />
                <div class="form-element">
                    <label for="yarnWeight">Finished Yarn:</label>
                    <select v-model="this.yarnWeight">
                        <option value="null" selected disabled hidden>—</option>
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
                <div class="form-element">
                    <label for="finishedLength">Finished Yarn Length:</label>
                    <div class="split-two">
                        <input
                            type="number"
                            placeholder="0"
                            v-model="this.finishedLength"
                        />
                        <select v-model="this.lengthUnit">
                            <option value="null" selected disabled hidden>
                                —
                            </option>
                            <option value="yd">yards</option>
                            <option value="m">meters</option>
                        </select>
                    </div>
                </div>
                <div class="form-element">
                    <label for="finishedWeight">Finished Yarn Weight:</label>
                    <div class="split-two">
                        <input
                            type="number"
                            placeholder="0"
                            v-model="this.finishedWeight"
                        />
                        <select v-model="this.weightUnit">
                            <option value="null" selected disabled hidden>
                                —
                            </option>
                            <option value="oz">oz</option>
                            <option value="g">grams</option>
                        </select>
                    </div>
                </div>
                <div class="form-element">
                    <label for="grist">Grist:</label>
                    <div class="split-two">
                        <input
                            type="number"
                            placeholder="0"
                            v-model="this.grist"
                        />
                        <select v-model="this.gristUnit">
                            <option value="null" selected disabled hidden>
                                —
                            </option>
                            <option value="ypp">YPP</option>
                            <option value="mpk">MPK</option>
                        </select>
                    </div>
                </div>
                <div class="form-element">
                    <label for="wpi">WPI (Wraps Per Inch):</label>
                    <input type="number" placeholder="0" v-model="this.wpi" />
                </div>
                <div class="form-element">
                    <label for="pliesCount"># of Plies:</label>
                    <input
                        type="number"
                        placeholder="0"
                        v-model="this.pliesCount"
                    />
                </div>
                <div class="form-element">
                    <label for="twistDirection">Twist Direction:</label>
                    <div class="split-two" id="twist-direction-container">
                        <div>
                            <label for="twistDirectionSingles">Singles:</label>
                            <select v-model="this.twistDirectionSingles">
                                <option value="null" selected disabled hidden>
                                    —
                                </option>
                                <option value="s">S</option>
                                <option value="z">Z</option>
                            </select>
                        </div>
                        <div>
                            <label for="twistDirectionsPlied">Plied:</label>
                            <select v-model="this.twistDirectionPlied">
                                <option value="null" selected disabled hidden>
                                    —
                                </option>
                                <option value="s">S</option>
                                <option value="z">Z</option>
                            </select>
                        </div>
                    </div>
                </div>
                <div class="form-element">
                    <label for="twistAngle">Twist Angle:</label>
                    <input
                        type="number"
                        placeholder="0"
                        v-model="this.twistAngle"
                    />
                </div>
                <div class="form-element">
                    <label for="driveRatios">Drive Ratios:</label>
                    <div class="split-two" id="drive-ratios-container">
                        <div>
                            <label for="driveRatioSingles">Singles:</label>
                            <input
                                type="number"
                                placeholder="0"
                                v-model="this.driveRatioSingles"
                            />
                        </div>
                        <div>
                            <label for="driveRatioPlied">Plied:</label>
                            <input
                                type="number"
                                placeholder="0"
                                v-model="this.driveRatioPlied"
                            />
                        </div>
                    </div>
                </div>
            </span>

            <!-- WEAVING -->
            <span v-if="this.weaving">
                <div class="divider" />
                <div class="form-element">
                    <label for="warpYarn">Warp Yarn:</label>
                    <input
                        type="text"
                        placeholder="Warp yarn information"
                        v-model="this.warpYarn"
                    />
                </div>
                <div class="form-element">
                    <label for="weftYarn">Weft Yarn:</label>
                    <input
                        type="text"
                        placeholder="Weft yarn information"
                        v-model="this.weftYarn"
                    />
                </div>
                <div class="form-element">
                    <label for="epi">EPI (Ends Per Inch):</label>
                    <input
                        type="number"
                        step="0.01"
                        placeholder="0"
                        v-model="this.epi"
                    />
                </div>
                <div class="form-element">
                    <label for="totalEnds">Total Ends:</label>
                    <input
                        type="number"
                        placeholder="0"
                        v-model="this.totalEnds"
                    />
                </div>
                <div class="form-element">
                    <label for="ppi">PPI (Picks Per Inch):</label>
                    <input
                        type="number"
                        step="0.01"
                        placeholder="0"
                        v-model="this.ppi"
                    />
                </div>
                <div class="form-element">
                    <label for="draftNotes">Draft Notes:</label>
                    <textarea
                        placeholder="Enter notes for your project's draft"
                        v-model="this.draftNotes"
                    />
                </div>
                <div class="form-element">
                    <label for="widthInReed">Width In Reed:</label>
                    <input
                        type="number"
                        step="0.01"
                        placeholder="0"
                        v-model="this.widthInReed"
                    />
                </div>
                <div class="form-element">
                    <label for="length">Length:</label>
                    <div class="input-select">
                        <input
                            type="number"
                            step="0.01"
                            placeholder="0"
                            v-model="this.length"
                        />
                        <select v-model="this.lengthUnit">
                            <option value="null" selected disabled hidden>
                                —
                            </option>
                            <option value="in">inches</option>
                            <option value="cm">centimeters</option>
                        </select>
                    </div>
                </div>
                <div class="form-element">
                    <label for="finishedLength">Finished Length:</label>
                    <div class="input-select">
                        <input
                            type="number"
                            step="0.01"
                            placeholder="0"
                            v-model="this.finishedLength"
                        />
                        <p v-if="this.lengthUnit == 'in'">inches</p>
                        <p v-else-if="this.lengthUnit == 'cm'">centimeters</p>
                        <p v-else>—</p>
                    </div>
                </div>
            </span>

            <!-- KNITTING -->
            <span v-if="this.knitting">
                <div class="divider" />
                <div class="form-element">
                    <label for="sizeMade">Size Made:</label>
                    <input
                        type="text"
                        placeholder="Enter size information"
                        v-model="this.sizeMade"
                    />
                </div>
                <div class="form-element">
                    <label for="needles">Needles Used:</label>
                    <input
                        type="text"
                        placeholder="Enter comma-separated needle sizes"
                        v-model="this.needleSizes"
                    />
                </div>
                <div class="form-element">
                    <label for="gauge">Gauge:</label>
                    <div id="gauge-container">
                        <div id="gauge-container-row1">
                            <input
                                type="number"
                                placeholder="0"
                                v-model="this.gaugeCount"
                            />
                            <select v-model="this.gaugeUnit">
                                <option value="null" selected disabled hidden>
                                    —
                                </option>
                                <option value="sts">stitches</option>
                                <option value="reps">repeats</option>
                            </select>
                            <p>and</p>
                            <input
                                type="number"
                                placeholder="0"
                                v-model="this.gaugeRows"
                            />
                            <p>rows/rounds</p>
                        </div>
                        <div id="gauge-container-row2">
                            <p>/</p>
                            <input
                                type="number"
                                placeholder="0"
                                v-model="this.gaugeSizeWidth"
                            />
                            <p>x</p>
                            <input
                                type="number"
                                placeholder="0"
                                v-model="this.gaugeSizeHeight"
                            />
                            <select v-model="this.gaugeSizeUnit">
                                <option value="null" selected disabled hidden>
                                    —
                                </option>
                                <option value="in">inches</option>
                                <option value="cm">centimeters</option>
                            </select>
                        </div>
                    </div>
                </div>
            </span>

            <!-- CROCHETING -->
            <span v-if="this.crocheting">
                <div class="divider" />
            </span>

            <!-- SEWING -->
            <span v-if="this.sewing && !this.knitting">
                <div class="divider" />
                <div class="form-element">
                    <label for="sizeMade">Size Made:</label>
                    <input
                        type="text"
                        placeholder="Enter size information"
                        v-model="this.sizeMade"
                    />
                </div>
            </span>

            <!-- EMBROIDERY -->
            <span v-if="this.embroidery">
                <div class="divider" />
            </span>

            <div class="divider" />
            <div class="form-element">
                <label for="tools">Linked Tools:</label>
                <div class="linked-div">
                    <span v-if="this.projectTools?.length">
                        <div
                            v-for="toolLink in this.projectTools"
                            :key="toolLink.id"
                            class="linked-item-display"
                        >
                            <div class="linked-item-display-left">
                                <img
                                    v-if="toolLink?.toolItem?.imageURL"
                                    :src="toolLink.toolItem.imageURL"
                                    alt="User-uploaded image of tool"
                                    @click="
                                        redirectToTool(toolLink.toolItem.id)
                                    "
                                />
                                <img
                                    v-else
                                    src="https://knotelry.s3.amazonaws.com/image-placeholder.png"
                                    alt="No image found"
                                    @click="
                                        redirectToTool(toolLink.toolItem.id)
                                    "
                                />
                                <p
                                    class="link"
                                    @click="
                                        redirectToTool(toolLink.toolItem.id)
                                    "
                                >
                                    {{ toolLink.toolItem.title }}
                                </p>
                            </div>
                            <p
                                class="unlink-item"
                                :id="toolLink.id"
                                @click="unlinkTool"
                            >
                                Unlink
                            </p>
                        </div>
                    </span>
                    <span v-else>
                        <p>No tools linked</p>
                    </span>
                    <div class="search-field">
                        <input
                            type="text"
                            class="search-link"
                            placeholder="Search toolbox"
                            @keyup="dynamicSearchTools"
                            v-model="this.searchToolParam"
                        />
                        <div
                            class="search-results"
                            v-if="this.searchToolParam?.length"
                        >
                            <div
                                v-if="
                                    this.searchToolParam?.length &&
                                    this.searchTools?.length
                                "
                            >
                                <div
                                    v-for="tool in this.searchTools"
                                    :key="tool.id"
                                    class="linked-item-display"
                                >
                                    <div class="linked-item-display-left">
                                        <img
                                            v-if="tool?.imageURL"
                                            :src="tool.imageURL"
                                            alt="User-uploaded image of tool"
                                        />
                                        <img
                                            v-else
                                            src="https://knotelry.s3.amazonaws.com/image-placeholder.png"
                                            alt="No image found"
                                            @click="
                                                redirectToStash(
                                                    stashLink.stashItem.id
                                                )
                                            "
                                        />
                                        <p>{{ tool.title }}</p>
                                    </div>
                                    <p
                                        class="link-item"
                                        @click="linkTool"
                                        :id="tool.id"
                                    >
                                        Link
                                    </p>
                                </div>
                            </div>
                            <div v-else-if="this.searchToolParam?.length">
                                No results found!
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Linked Materials -->
            <div class="form-element">
                <label for="materials">Linked Materials:</label>
                <div class="linked-div">
                    <span v-if="this.projectMaterials?.length">
                        <div
                            v-for="materialLink in this.projectMaterials"
                            :key="materialLink.id"
                            class="material-display"
                        >
                            <div class="linked-item-display">
                                <div class="linked-item-display-left">
                                    <img
                                        v-if="
                                            materialLink?.stashItem
                                                ?.stashItemImages?.length
                                        "
                                        :src="
                                            materialLink.stashItem
                                                .stashItemImages[0].imageURL
                                        "
                                        @click="
                                            redirectToStash(
                                                materialLink.stashItem.id
                                            )
                                        "
                                        alt="User-uploaded image of stash item"
                                    />
                                    <img
                                        v-else
                                        src="https://knotelry.s3.amazonaws.com/image-placeholder.png"
                                        alt="No image found"
                                    />
                                    <div class="material-text">
                                        <p
                                            class="link"
                                            @click="
                                                redirectToStash(
                                                    materialLink.stashItem.id
                                                )
                                            "
                                        >
                                            {{ materialLink.stashItem.title }}
                                        </p>
                                        <p
                                            v-if="
                                                materialLink.stashItem.type ==
                                                'fiber'
                                            "
                                        >
                                            {{ materialLink.fiberQuantityUsed }}
                                            {{ materialLink.fiberQuantityUnit }}
                                            used
                                        </p>
                                        <p
                                            v-if="
                                                materialLink.stashItem.type ==
                                                'yarn'
                                            "
                                        >
                                            {{ materialLink.lengthUsed }}
                                            {{ materialLink.lengthUnit }} used
                                        </p>
                                    </div>
                                </div>
                                <div class="linked-materials-options">
                                    <p
                                        class="unlink-item"
                                        :id="materialLink.id"
                                        @click="expandAdjustMaterial"
                                    >
                                        Edit Details
                                    </p>
                                    <p
                                        class="unlink-item"
                                        :id="materialLink.id"
                                        @click="unlinkMaterial"
                                    >
                                        Unlink
                                    </p>
                                </div>
                            </div>
                            <div
                                class="material-edit-container hidden"
                                :id="`material-edit-container-${materialLink.id}`"
                            >
                                <span
                                    v-if="
                                        materialLink?.stashItem?.type == 'fiber'
                                    "
                                >
                                    <div
                                        class="material-edit-form"
                                        :id="`material-edit-form-${materialLink.id}`"
                                    >
                                        <div>
                                            <input
                                                type="number"
                                                v-model="
                                                    materialLink.fiberQuantityUsed
                                                "
                                                :id="`fiberQuantityUsed-${materialLink.id}`"
                                            />
                                            <select
                                                v-model="
                                                    materialLink.fiberQuantityUnit
                                                "
                                                :id="`fiberQuantityUnit-${materialLink.id}`"
                                            >
                                                <option
                                                    value="null"
                                                    selected
                                                    disabled
                                                    hidden
                                                >
                                                    —
                                                </option>
                                                <option value="oz">oz</option>
                                                <option value="g">grams</option>
                                            </select>
                                            <p>used</p>
                                        </div>
                                        <p
                                            class="unlink-item"
                                            :key="materialLink.id"
                                            @click="
                                                submitMaterialEdit(
                                                    materialLink.id
                                                )
                                            "
                                        >
                                            Submit Edit
                                        </p>
                                    </div>
                                </span>
                                <span
                                    v-else-if="
                                        materialLink?.stashItem?.type ==
                                            'yarn' ||
                                        materialLink?.stashItem?.type ==
                                            'fabric' ||
                                        materialLink?.stashItem?.type ==
                                            'thread'
                                    "
                                >
                                    <div
                                        class="material-edit-form"
                                        :id="`material-edit-form-${materialLink.id}`"
                                    >
                                        <div>
                                            <input
                                                type="number"
                                                v-model="
                                                    materialLink.lengthUsed
                                                "
                                                :id="`lengthUsed-${materialLink.id}`"
                                            />
                                            <select
                                                v-model="
                                                    materialLink.lengthUnit
                                                "
                                                :id="`lengthUnit-${materialLink.id}`"
                                            >
                                                <option
                                                    value="null"
                                                    selected
                                                    disabled
                                                    hidden
                                                >
                                                    —
                                                </option>
                                                <option value="yd">
                                                    yards
                                                </option>
                                                <option value="m">
                                                    meters
                                                </option>
                                            </select>
                                            <p>used</p>
                                        </div>
                                        <p
                                            class="unlink-item"
                                            :key="materialLink.id"
                                            @click="
                                                submitMaterialEdit(
                                                    materialLink.id
                                                )
                                            "
                                        >
                                            Submit Edit
                                        </p>
                                    </div>
                                </span>
                            </div>
                        </div>
                    </span>
                    <span v-else>
                        <p>No materials linked</p>
                    </span>
                    <div class="search-field">
                        <input
                            type="text"
                            class="search-link"
                            placeholder="Search stash"
                            @keyup="dynamicSearchStash"
                            v-model="this.searchStashParam"
                        />
                        <div
                            class="search-results"
                            v-if="this.searchStashParam?.length"
                        >
                            <div
                                v-if="
                                    this.searchStashParam?.length &&
                                    this.searchStash?.length
                                "
                            >
                                <div
                                    v-for="stashItem in this.searchStash"
                                    :key="stashItem.id"
                                    class="linked-item-display"
                                >
                                    <div class="linked-item-display-left">
                                        <img
                                            v-if="
                                                stashItem?.stashItemImages
                                                    ?.length
                                            "
                                            :src="
                                                stashItem.stashItemImages[0]
                                                    .imageURL
                                            "
                                            alt="User-uploaded image of stash item"
                                        />
                                        <img
                                            v-else
                                            src="https://knotelry.s3.amazonaws.com/image-placeholder.png"
                                            alt="No image found"
                                        />
                                        <p>{{ stashItem.title }}</p>
                                    </div>
                                    <p
                                        class="link-item"
                                        @click="linkMaterial"
                                        :id="stashItem.id"
                                    >
                                        Link
                                    </p>
                                </div>
                            </div>
                            <div v-else-if="this.searchStashParam?.length">
                                No results found!
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="form-element">
                <div />
                <div class="option-buttons">
                    <button type="button" id="submit" @click="submit">
                        Edit
                    </button>
                    <p class="option-button" id="cancel" @click="cancel">
                        Cancel
                    </p>
                    <p class="option-button" id="delete" @click="deleteProject">
                        Delete
                    </p>
                </div>
            </div>
        </form>
    </div>
</template>

<script>
export default {
    name: "ProjectEdit",
    data() {
        return {
            validationErrors: [],
            id: this.$route.params.projectId,
            title: null,
            description: null,
            craftTypes: null,
            patternName: null,
            patternAuthor: null,
            linkToPattern: null,
            sizeMade: null,
            spinning: false,
            weaving: false,
            knitting: false,
            crocheting: false,
            sewing: false,
            embroidery: false,

            tags: null,
            status: null,
            attributes: null,
            storedIn: null,

            startDate: null,
            endDate: null,

            yarnWeight: null,
            grist: null,
            gristUnit: null,
            wpi: null,
            pliesCount: null,

            twistDirectionSingles: null,
            twistDirectionPlied: null,
            twistAngle: null,
            driveRatioSingles: null,
            driveRatioPlied: null,
            finishedWeight: null,
            weightUnit: null,

            warpYarn: null,
            weftYarn: null,
            epi: null,
            totalEnds: null,
            ppi: null,
            draftNotes: null,
            widthInReed: null,
            length: null,
            lengthUnit: null,
            finishedLength: null,

            needleSizes: null,
            gaugeCount: null,
            gaugeUnit: null,
            gaugeRows: null,
            gaugeSizeWidth: null,
            gaugeSizeHeight: null,
            gaugeSizeUnit: null,

            notes: null,

            image: null,
            imageURL: "",
            imageStatus: "Upload",

            user: null,
            projectMaterials: [],
            projectTools: [],
            projectImages: [],

            searchToolParam: "",
            searchTools: [],
            usersTools: [],

            searchStashParam: "",
            searchStash: [],
            usersStash: [],
        };
    },
    mounted() {
        const data = loadProject(this.$route.params.projectId).then((data) => {
            if (data && data?.userId == this.$store.state.sessionUser?.id) {
                this.title = data.title;
                this.description = data.description;

                this.craftTypes = data.craftTypes?.split(" ");
                this.spinning = this.craftTypes?.includes("spinning");
                this.weaving = this.craftTypes?.includes("weaving");
                this.knitting = this.craftTypes?.includes("knitting");
                this.crocheting = this.craftTypes?.includes("crocheting");
                this.sewing = this.craftTypes?.includes("sewing");
                this.embroidery = this.craftTypes?.includes("embroidery");

                this.patternName = data.patternName;
                this.patternAuthor = data.patternAuthor;
                this.linkToPattern = data.linkToPattern;
                this.sizeMade = data.sizeMade;
                this.tags = data.tags;
                this.status = data.status;
                this.attributes = data.attributes;
                this.storedIn = data.storedIn;

                if (data.startDate) this.startDate = formatDate(data.startDate);
                if (data.endDate) this.endDate = formatDate(data.endDate);

                this.yarnWeight = data.yarnWeight;
                this.grist = data.grist;
                this.gristUnit = data.gristUnit;
                this.wpi = data.wpi;
                this.pliesCount = data.pliesCount;
                this.twistDirectionSingles = data.twistDirectionSingles;
                this.twistDirectionPlied = data.twistDirectionPlied;
                this.twistAngle = data.twistAngle;
                this.driveRatioSingles = data.driveRatioSingles;
                this.driveRatioPlied = data.driveRatioPlied;
                this.finishedWeight = data.finishedWeight;
                this.weightUnit = data.weightUnit;

                this.warpYarn = data.warpYarn;
                this.weftYarn = data.weftYarn;
                this.epi = data.epi;
                this.totalEnds = data.totalEnds;
                this.ppi = data.ppi;
                this.draftNotes = data.draftNotes;
                this.widthInReed = data.widthInReed;
                this.length = data.length;
                this.lengthUnit = data.lengthUnit;
                this.finishedLength = data.finishedLength;

                this.needleSizes = data.needleSizes;
                this.gaugeCount = data.gaugeCount;
                this.gaugeUnit = data.gaugeUnit;
                this.gaugeRows = data.gaugeRows;
                this.gaugeSizeWidth = data.gaugeSizeWidth;
                this.gaugeSizeHeight = data.gaugeSizeHeight;
                this.gaugeSizeUnit = data.gaugeSizeUnit;

                this.notes = data.notes;
                this.createdAt = data.createdAt;
                this.updatedAt = data.updatedAt;

                this.user = data.user;
                this.projectMaterials = data.projectMaterials;
                this.projectTools = data.projectTools;
                this.projectImages = data.projectImages;

                const toolsData = loadUsersTools(
                    this.$store.state.sessionUser?.id
                ).then((toolsData) => {
                    if (toolsData) {
                        this.usersTools = Object.values(toolsData)[0];
                    }
                });

                const stashData = loadUsersStash(
                    this.$store.state.sessionUser?.id
                ).then((stashData) => {
                    if (stashData) {
                        this.usersStash = Object.values(stashData)[0];
                    }
                });
            } else {
                this.$router.push("/404");
            }
        });
    },
    methods: {
        async submit() {
            this.validationErrors = [];
            const errorsArr = [];
            if (!this.title || this.title?.length == 0)
                errorsArr.push("Title cannot be empty.");
            if (this.title?.length > 100)
                errorsArr.push("Title cannot be longer than 100 characters.");

            if (errorsArr.length > 0) {
                this.validationErrors = errorsArr;
                window.scrollTo(0, 0);
            } else {
                let craftTypes = "";

                if (this.spinning) craftTypes += "spinning ";
                if (this.weaving) craftTypes += "weaving ";
                if (this.knitting) craftTypes += "knitting ";
                if (this.crocheting) craftTypes += "crocheting ";
                if (this.sewing) craftTypes += "sewing ";
                if (this.embroidery) craftTypes += "embroidery ";

                craftTypes = craftTypes.slice(0, -1);

                const project = {
                    id: this.id,
                    title: this.title,
                    description: this.description,
                    craft_types: craftTypes,
                    pattern_name: this.patternName,
                    pattern_author: this.patternAuthor,
                    link_to_pattern: this.linkToPattern,
                    size_made: this.sizeMade,
                    tags: this.tags,
                    status: this.status,
                    attributes: this.attributes,
                    stored_in: this.storedIn,
                    start_date: this.startDate,
                    end_date: this.endDate,

                    yarn_weight: this.yarnWeight,
                    grist: this.grist,
                    grist_unit: this.gristUnit,
                    wpi: this.wpi,
                    plies_count: this.pliesCount,
                    twist_direction_singles: this.twistDirectionSingles,
                    twist_direction_plied: this.twistDirectionPlied,
                    twist_angle: this.twistAngle,
                    drive_ratio_singles: this.driveRatioSingles,
                    drive_ratio_plied: this.driveRatioPlied,
                    finished_weight: this.finishedWeight,
                    weight_unit: this.weightUnit,

                    warp_yarn: this.warpYarn,
                    weft_yarn: this.weftYarn,
                    epi: this.epi,
                    total_ends: this.totalEnds,
                    ppi: this.ppi,
                    draft_notes: this.draftNotes,
                    width_in_reed: this.widthInReed,
                    length: this.length,
                    length_unit: this.lengthUnit,
                    finished_length: this.finishedLength,

                    needle_sizes: this.needleSizes,
                    gauge_count: this.gaugeCount,
                    gauge_unit: this.gaugeUnit,
                    gauge_rows: this.gaugeRows,
                    gauge_size_width: this.gaugeSizeWidth,
                    gauge_size_height: this.gaugeSizeHeight,
                    gauge_size_unit: this.gaugeSizeUnit,

                    notes: this.notes,
                };
                const response = await fetch("/api/projects/", {
                    method: "PUT",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(project),
                });
                if (response.ok) {
                    const data = await response.json();
                    this.$router.push(`/projects/${data.id}`);
                }
            }
        },
        cancel() {
            this.$router.push(`/projects/${this.id}`);
        },
        deleteProject() {
            this.$router.push(
                `/projects/${this.$route.params.projectId}/delete`
            );
        },
        setImage($event) {
            this.image = $event.target.files[0];
        },
        async uploadImage($event, image) {
            $event.preventDefault();
            this.imageStatus = "Loading...";
            const formData = new FormData();
            formData.append("image", image);

            const res = await fetch("/api/images", {
                method: "POST",
                body: formData,
            });

            if (res.ok) {
                const data = await res.json().then(async (data) => {
                    const image = {
                        project_id: this.$route.params.projectId,
                        image_url: data.url,
                    };
                    const response = await fetch("/api/projects/images/", {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json",
                        },
                        body: JSON.stringify(image),
                    });
                    if (response.ok) {
                        const imageData = loadLinkedImages(
                            parseInt(this.$route.params.projectId)
                        ).then((imageData) => {
                            this.projectImages = imageData.linkedImages;
                        });
                    }
                });
                this.imageStatus = "Uploaded!";
            } else {
                this.imageStatus = "Image not found / Invalid image!";
            }
        },
        async deleteImage($event) {
            $event.preventDefault();

            const response = await fetch("/api/projects/images/", {
                method: "DELETE",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    id: parseInt($event.target.id),
                }),
            });
            if (response.ok) {
                const imageData = loadLinkedImages(
                    parseInt(this.$route.params.projectId)
                ).then((imageData) => {
                    this.projectImages = imageData.linkedImages;
                });
            }
        },
        dynamicSearchTools($event) {
            $event.preventDefault();
            this.searchToolParam = $event.target.value;
            this.searchTools = [];
            const temp = [];
            this.usersTools.forEach((tool) => {
                if (tool.title) {
                    if (
                        tool.title
                            .toLowerCase()
                            ?.includes(this.searchToolParam?.toLowerCase())
                    ) {
                        temp.push(tool);
                    }
                } else if (tool.description) {
                    if (
                        tool.description
                            .toLowerCase()
                            ?.includes(this.searchToolParam?.toLowerCase())
                    ) {
                        temp.push(tool);
                    }
                }
            });
            this.searchTools = temp;
        },
        async unlinkTool($event) {
            const response = await fetch(`/api/projects/tools/`, {
                method: "DELETE",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    id: $event.target.id,
                }),
            });
            if (response.ok) {
                const toolData = loadLinkedTools(
                    parseInt(this.$route.params.projectId)
                ).then((toolData) => {
                    this.projectTools = toolData.linkedTools;
                });
            }
        },
        async linkTool($event) {
            const response = await fetch(`/api/projects/tools/`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    project_id: parseInt(this.$route.params.projectId),
                    tool_id: parseInt($event.target.id),
                }),
            });
            if (response.ok) {
                const toolData = loadLinkedTools(
                    parseInt(this.$route.params.projectId)
                ).then((toolData) => {
                    this.projectTools = toolData.linkedTools;
                    this.searchToolParam = "";
                });
            }
        },
        dynamicSearchStash($event) {
            $event.preventDefault();
            this.searchStashParam = $event.target.value;
            this.searchStash = [];
            const temp = [];
            this.usersStash.forEach((stashItem) => {
                if (stashItem.title) {
                    if (
                        stashItem.title
                            .toLowerCase()
                            ?.includes(this.searchStashParam?.toLowerCase())
                    ) {
                        temp.push(stashItem);
                    }
                } else if (stashItem.description) {
                    if (
                        stashItem.description
                            .toLowerCase()
                            ?.includes(this.searchStashParam?.toLowerCase())
                    ) {
                        temp.push(stashItem);
                    }
                }
            });
            this.searchStash = temp;
        },
        async unlinkMaterial($event) {
            const response = await fetch(`/api/projects/materials/`, {
                method: "DELETE",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    id: $event.target.id,
                }),
            });
            if (response.ok) {
                const materialsData = loadLinkedMaterials(
                    parseInt(this.$route.params.projectId)
                ).then((materialsData) => {
                    this.projectMaterials = materialsData.linkedMaterials;
                });
            }
        },
        async linkMaterial($event) {
            const response = await fetch(`/api/projects/materials/`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    project_id: parseInt(this.$route.params.projectId),
                    stash_id: parseInt($event.target.id),
                    fiber_quantity_used: null,
                    fiber_quantity_unit: null,
                    length_used: null,
                    length_unit: null,
                    weight_used: null,
                    weight_unit: null,
                    skeins_used: null,
                }),
            });
            if (response.ok) {
                const materialsData = loadLinkedMaterials(
                    parseInt(this.$route.params.projectId)
                ).then((materialsData) => {
                    this.projectMaterials = materialsData.linkedMaterials;
                    this.searchStashParam = "";
                });
            }
        },
        expandAdjustMaterial($event) {
            $event.preventDefault();
            document
                .getElementById(`material-edit-container-${$event.target.id}`)
                .classList.remove("hidden");
        },
        async submitMaterialEdit(id) {
            const updatedMaterial = {
                id: id,
                fiber_quantity_used: null,
                fiber_quantity_unit: null,
                length_used: null,
                length_unit: null,
                weight_used: null,
                weight_unit: null,
                skeins_used: null,
            };
            if (
                document.getElementById(`fiberQuantityUsed-${id}`) &&
                document.getElementById(`fiberQuantityUsed-${id}`).value
            ) {
                updatedMaterial.fiber_quantity_used = document.getElementById(
                    `fiberQuantityUsed-${id}`
                ).value;
            }
            if (
                document.getElementById(`fiberQuantityUnit-${id}`) &&
                document.getElementById(`fiberQuantityUnit-${id}`).value
            ) {
                updatedMaterial.fiber_quantity_unit = document.getElementById(
                    `fiberQuantityUnit-${id}`
                ).value;
            }
            if (
                document.getElementById(`lengthUsed-${id}`) &&
                document.getElementById(`lengthUsed-${id}`).value
            ) {
                updatedMaterial.length_used = document.getElementById(
                    `lengthUsed-${id}`
                ).value;
            }
            if (
                document.getElementById(`lengthUnit-${id}`) &&
                document.getElementById(`lengthUnit-${id}`).value
            ) {
                updatedMaterial.length_unit = document.getElementById(
                    `lengthUnit-${id}`
                ).value;
            }
            if (
                document.getElementById(`weightUsed-${id}`) &&
                document.getElementById(`weightUsed-${id}`).value
            ) {
                updatedMaterial.weight_used = document.getElementById(
                    `weightUsed-${id}`
                ).value;
            }
            if (
                document.getElementById(`weightUnit-${id}`) &&
                document.getElementById(`weightUnit-${id}`).value
            ) {
                updatedMaterial.weight_unit = document.getElementById(
                    `weightUnit-${id}`
                ).value;
            }
            if (
                document.getElementById(`skeinsUsed-${id}`) &&
                document.getElementById(`skeinsUsed-${id}`).value
            ) {
                updatedMaterial.skeins_used = document.getElementById(
                    `skeinsUsed-${id}`
                ).value;
            }

            const response = await fetch("/api/projects/materials/", {
                method: "PUT",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(updatedMaterial),
            });

            if (response.ok) {
                const materialsData = loadLinkedMaterials(
                    parseInt(this.$route.params.projectId)
                ).then((materialsData) => {
                    this.projectMaterials = materialsData.linkedMaterials;
                    document
                        .getElementById(`material-edit-container-${id}`)
                        .classList.add("hidden");
                });
            }
        },
        redirectToStash(id) {
            this.$router.push(`/stash/${id}`);
        },
        redirectToTool(id) {
            this.$router.push(`/tools/${id}`);
        },
    },
};

const loadProject = async (id) => {
    const response = await fetch(`/api/projects/${id}`);
    if (response.ok) {
        const data = await response.json();
        return data;
    } else {
        const data = false;
        return data;
    }
};

const loadLinkedImages = async (id) => {
    const response = await fetch(`/api/projects/${id}/images`);
    if (response.ok) {
        const data = await response.json();
        return data;
    } else {
        const data = false;
        return data;
    }
};

const loadLinkedTools = async (id) => {
    const response = await fetch(`/api/projects/${id}/tools`);
    if (response.ok) {
        const data = await response.json();
        return data;
    } else {
        const data = false;
        return data;
    }
};

const loadLinkedMaterials = async (id) => {
    const response = await fetch(`/api/projects/${id}/materials`);
    if (response.ok) {
        const data = await response.json();
        return data;
    } else {
        const data = false;
        return data;
    }
};

const loadUsersTools = async (userId) => {
    const response = await fetch(`/api/tools/users/${userId}`);
    if (response.ok) {
        const toolsData = await response.json();
        return toolsData;
    } else {
        return false;
    }
};

const loadUsersStash = async (userId) => {
    const response = await fetch(`/api/stash/users/${userId}`);
    if (response.ok) {
        const stashData = await response.json();
        return stashData;
    } else {
        const stashData = false;
        return false;
    }
};

const formatDate = (date) => {
    const d = new Date(date);
    return d.toISOString().split("T")[0];
};
</script>

<style scoped>
.project-form-body {
    display: grid;
    grid-template-columns: 250px 1fr;
    column-gap: 100px;
    padding-left: 8%;
    padding-right: 8%;
    padding-top: 60px;
}

.left {
    display: flex;
    flex-direction: column;
    padding-bottom: 32px;
    padding-top: 32px;
}

.image-container {
    position: relative;
    margin-top: 8px;
    margin-bottom: 8px;
}

.fa-trash-alt {
    position: absolute;
    right: 5%;
    bottom: 5%;
    color: var(--color-nav);
    text-shadow: 0px 0px 10px var(--color-shadow);
    font-size: 20px;
}

.fa-trash-alt:hover {
    cursor: pointer;
}

.project-image {
    margin-left: auto;
    margin-right: auto;
    height: 100%;
    width: 100%;
    object-fit: cover;
    border: 1px solid var(--color-shadow);
    border-radius: 6px;
}

#image-upload-button {
    margin-top: 8px;
    width: 100%;
}

.project-form {
    font-family: "Open Sans", sans-serif;
    padding-bottom: 32px;
    font-size: 14px;
}

.form-element {
    display: grid;
    grid-template-columns: 150px 1fr;
    column-gap: 16px;
    margin-bottom: 6px;
    align-items: center;
}

label {
    text-align: justify;
    align-self: middle;
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
    margin-top: 0px;
    margin-bottom: 0px;
}

textarea {
    font-size: 14px;
    font-family: "Open Sans", sans-serif;
    border-radius: 6px;
    border: 1px solid var(--color-shadow);
    padding-top: 6px;
    padding-bottom: 6px;
    padding-left: 10px;
    padding-right: 10px;
    resize: vertical;
    min-height: 100px;
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
}

button:hover {
    cursor: pointer;
}

button:active {
    box-shadow: 2px 2px 2px var(--color-shadow);
}

#submit {
    width: 100%;
    margin-top: 6px;
    font-weight: normal;
    letter-spacing: 2px;
    color: white;
    background-color: var(--color-primary-contrast);
    margin-bottom: 48px;
}

.error-container {
    display: flex;
    flex-direction: column;
    margin: 0px;
    text-align: center;
}

.error {
    color: var(--color-primary-contrast);
    font-size: 16px;
    font-weight: bold;
    text-align: center;
}

.option-buttons {
    width: 100%;
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    column-gap: 4px;
}

.option-button {
    width: 100%;
    margin-top: 6px;
    font-weight: normal;
    letter-spacing: 1.5px;
    color: var(--color-primary-contrast);
    background-color: white;
    margin-bottom: 48px;
    font-family: "Open Sans", sans-serif;
    padding-top: 4px;
    padding-bottom: 4px;
    border-radius: 4px;
    border: 1px solid var(--color-shadow);
    box-shadow: 1px 1px 1px var(--color-shadow);
}

.option-button:hover {
    cursor: pointer;
}

.option-button:active {
    box-shadow: 2px 2px 2px var(--color-shadow);
}

#delete {
    background-color: var(--color-primary-contrast);
    color: white;
}

#pattern-div {
    display: flex;
    column-gap: 8px;
    align-items: center;
}

#pattern-div > p {
    margin: 0px;
}

#pattern-div > input {
    width: 100%;
}

#pattern-link {
    display: grid;
    grid-template-columns: 110px 1fr;
    column-gap: 8px;
    align-items: center;
}

#pattern-link > p {
    margin: 0px;
}

.craft-options {
    display: grid;
    grid-template-columns: repeat(auto-fill, 150px);
    justify-content: space-between;
    row-gap: 2px;
    padding-top: 4px;
}

.craft-options > button {
    font-size: 12px;
    letter-spacing: 0px;
    margin: 2px;
}

.selected {
    background-color: var(--color-primary-contrast);
    color: white;
}

.split-two {
    display: grid;
    grid-template-columns: 1fr 1fr;
    column-gap: 8%;
}

.split-two > input {
    width: 100%;
}

.split-two > select {
    width: 100%;
}

#project-dates-container > div {
    display: grid;
    grid-template-columns: 46px 1fr;
    justify-content: space-between;
    align-items: center;
}

#twist-direction-container {
    width: 100%;
    display: grid;
    grid-template-columns: 1fr 1fr;
    column-gap: 10%;
}

#twist-direction-container > div {
    display: flex;
    flex-direction: row;
    align-items: center;
    column-gap: 8%;
}

#twist-direction-container > div > select {
    width: 100%;
}

#drive-ratios-container {
    width: 100%;
    display: grid;
    grid-template-columns: 1fr 1fr;
    column-gap: 10%;
}

#drive-ratios-container > div {
    display: flex;
    flex-direction: row;
    align-items: center;
    column-gap: 8%;
}

#drive-ratios-container > div > input {
    width: 100%;
}

#gauge-container {
    display: flex;
    flex-direction: column;
}

#gauge-container-row1 {
    display: flex;
    flex-direction: row;
    column-gap: 4px;
    align-items: center;
}

#gauge-container-row1 > input {
    width: 32px;
}

#gauge-container-row1 > p {
    margin-top: 0px;
    margin-bottom: 0px;
}

#gauge-container-row2 {
    display: flex;
    flex-direction: row;
    column-gap: 4px;
    align-items: center;
}

#gauge-container-row2 > input {
    width: 32px;
}

#gauge-container-row2 > select {
    width: 100%;
}

.search-field {
    margin-bottom: 12px;
    margin-top: 12px;
    justify-content: center;
    width: 100%;
}

.search-link {
    width: 100%;
    box-sizing: border-box;
}

.search-results {
    margin-left: auto;
    margin-right: auto;
    padding-top: 8px;
}

.linked-div > span > p {
    text-align: left;
    align-self: flex-start;
    margin-top: 0px;
}

.linked-item-display {
    width: 100%;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    column-gap: 20px;
    margin-bottom: 6px;
}

.linked-item-display-left {
    display: flex;
    flex-direction: row;
    column-gap: 20px;
    text-align: left;
}

.linked-item-display-left > img {
    width: 50px;
    height: 50px;
    object-fit: cover;
    border: 1px solid var(--color-shadow);
    border-radius: 4px;
}

.linked-item-display-left > img:hover {
    cursor: pointer;
}

.linked-item-display-left > p {
    margin-top: 0px;
    margin-bottom: 0px;
    align-self: center;
}

.unlink-item,
.link-item {
    color: var(--color-primary-contrast);
    text-align: right;
}

.unlink-item:hover,
.link-item:hover {
    font-weight: bold;
    cursor: pointer;
}

.linked-materials-options {
    display: flex;
    flex-direction: column;
}

.linked-materials-options > p {
    margin-top: 0px;
    margin-bottom: 0px;
}

.material-display {
    display: flex;
    flex-direction: column;
}

.material-edit-form {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
}

.material-edit-form > div {
    display: flex;
    column-gap: 12px;
    justify-content: flex-start;
}

.material-edit-form > div > input {
    width: 60px;
}

.material-edit-form > p {
    margin-top: 0px;
    margin-bottom: 0px;
    align-self: center;
}

.material-edit-form > div > p {
    margin-top: 0px;
    margin-bottom: 0px;
    align-self: center;
}

.hidden {
    display: none;
}

.material-edit-container {
    margin-bottom: 12px;
}

.material-text {
    display: flex;
    flex-direction: column;
    align-self: center;
}

.material-text > p {
    margin-top: 0px;
    margin-bottom: 0px;
    text-align: left;
}

.divider {
    border-top: 1px solid var(--color-shadow);
    margin-top: 32px;
    margin-bottom: 32px;
    padding: 0px;
}

.link:hover {
    font-weight: bold;
    cursor: pointer;
}

.input-select {
    display: flex;
    flex-direction: row;
    width: 100%;
    column-gap: 16px;
}

.input-select > p {
    align-self: center;
    margin-top: 0px;
    margin-bottom: 0px;
}
</style>
