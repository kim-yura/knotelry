<template>
    <div class="project-detail">
        <div class="left">
            <div class="project-header">
                <h2>{{ this.title }}</h2>
            </div>
            <div
                v-if="$store.state.sessionUser?.id == this.user?.id"
                class="project-options"
            >
                <button @click="editProject">Edit</button>
                <button @click="deleteProject">Delete</button>
            </div>
            <p v-if="!this.projectImages || this.projectImages?.length == 0">
                No linked images
            </p>
            <img
                v-for="image in this.projectImages"
                :key="image.id"
                class="detail-image"
                :src="image.imageURL"
                alt="User uploaded image of project"
            />
        </div>
        <div class="right">
            <!-- METADATA -->
            <div class="detail-text">
                <div class="text-label">Pattern:</div>
                <div
                    class="text-content"
                    v-if="this.patternName && this.linkToPattern"
                >
                    <a :href="this.linkToPattern" target="_blank">{{
                        this.patternName
                    }}</a>
                    <span v-if="this.patternAuthor">
                        by {{ this.patternAuthor }}</span
                    >
                </div>
                <div class="text-content" v-else-if="this.patternName">
                    {{ this.patternName }}
                    <span v-if="this.patternAuthor">
                        by {{ this.patternAuthor }}</span
                    >
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
                <div class="text-content" v-if="this.status == 'queued'">
                    Queued
                </div>
                <div
                    class="text-content"
                    v-else-if="this.status == 'inProgress'"
                >
                    In Progress
                </div>
                <div class="text-content" v-else-if="this.status == 'finished'">
                    Finished
                </div>
                <div class="text-content" v-else-if="this.status == 'timeout'">
                    In Time-out
                </div>
                <div class="text-content" v-else>—</div>
            </div>
            <div class="detail-text">
                <div class="text-label">Tagged Crafts:</div>
                <div
                    class="attributes-container"
                    v-if="this.craftTypes?.length"
                >
                    <p
                        class="attribute-container"
                        v-for="craft in this.craftTypes"
                        :key="craft"
                    >
                        {{ craft }}
                    </p>
                </div>
                <div class="text-content" v-else>—</div>
            </div>
            <div class="detail-text">
                <div class="text-label">Tags:</div>
                <div class="attributes-container" v-if="this.tags">
                    <p
                        class="attribute-container"
                        v-for="tag in this.tags"
                        :key="tag"
                    >
                        {{ tag }}
                    </p>
                </div>
                <div class="text-content" v-else>—</div>
            </div>
            <div class="detail-text">
                <div class="text-label">Tagged Attributes:</div>
                <div class="attributes-container" v-if="this.attributes">
                    <p
                        class="attribute-container"
                        v-for="attribute in this.attributes"
                        :key="attribute"
                    >
                        {{ attribute }}
                    </p>
                </div>
                <div class="text-content" v-else>—</div>
            </div>
            <div class="detail-text">
                <div class="text-label">Stored In:</div>
                <div class="text-content" v-if="this.storedIn">
                    {{ this.storedIn }}
                </div>
                <div class="text-content" v-else>—</div>
            </div>
            <div class="detail-text">
                <div class="text-label">Started:</div>
                <div class="text-content" v-if="this.startDate">
                    {{ this.startDate.slice(5, 16) }}
                </div>
                <div class="text-content" v-else>—</div>
            </div>
            <div class="detail-text">
                <div class="text-label">Finished:</div>
                <div class="text-content" v-if="this.endDate">
                    {{ this.endDate.slice(5, 16) }}
                </div>
                <div class="text-content" v-else>—</div>
            </div>
            <div class="divider" />

            <!-- SPINNING -->
            <span v-if="this.craftTypes?.includes('spinning')">
                <div class="detail-text">
                    <div class="text-label">Finished Yarn:</div>
                    <div class="text-content" v-if="this.yarnWeight == 'lace'">
                        Lace
                    </div>
                    <div
                        class="text-content"
                        v-if="this.yarnWeight == 'lfingering'"
                    >
                        Light Fingering
                    </div>
                    <div
                        class="text-content"
                        v-if="this.yarnWeight == 'fingering'"
                    >
                        Fingering
                    </div>
                    <div
                        class="text-content"
                        v-else-if="this.yarnWeight == 'sport'"
                    >
                        Sport
                    </div>
                    <div
                        class="text-content"
                        v-else-if="this.yarnWeight == 'dk'"
                    >
                        DK
                    </div>
                    <div
                        class="text-content"
                        v-else-if="this.yarnWeight == 'worsted'"
                    >
                        Worsted
                    </div>
                    <div
                        class="text-content"
                        v-else-if="this.yarnWeight == 'aran'"
                    >
                        Aran
                    </div>
                    <div
                        class="text-content"
                        v-else-if="this.yarnWeight == 'bulky'"
                    >
                        Bulky
                    </div>
                    <div
                        class="text-content"
                        v-else-if="this.yarnWeight == 'sbulky'"
                    >
                        Super Bulky
                    </div>
                    <div class="text-content" v-else-if="!this.yarnWeight">
                        —
                    </div>
                </div>
                <div class="detail-text">
                    <div class="text-label">Finished Yarn Length:</div>
                    <div class="text-content" v-if="this.finishedYarnLength">
                        {{ this.finishedYarnLength }}
                        {{ this.finishedYarnLengthUnit }}
                    </div>
                    <div class="text-content" v-else>—</div>
                </div>
                <div class="detail-text">
                    <div class="text-label">Finished Yarn Weight:</div>
                    <div class="text-content" v-if="this.finishedYarnWeight">
                        {{ this.finishedYarnWeight }}
                        {{ this.finishedYarnWeightUnit }}
                    </div>
                    <div class="text-content" v-else>—</div>
                </div>
                <div class="detail-text">
                    <div class="text-label">Grist:</div>
                    <div class="text-content" v-if="this.grist">
                        {{ this.grist }} {{ this.grist_unit }}
                    </div>
                    <div class="text-content" v-else>—</div>
                </div>
                <div class="detail-text">
                    <div class="text-label">WPI:</div>
                    <div class="text-content" v-if="this.wpi">
                        {{ this.wpi }} WPI
                    </div>
                    <div class="text-content" v-else>—</div>
                </div>
                <div class="detail-text">
                    <div class="text-label"># of Plies:</div>
                    <div class="text-content" v-if="this.pliesCount">
                        {{ this.pliesCount }}
                    </div>
                    <div class="text-content" v-else>—</div>
                </div>
                <div class="detail-text">
                    <div class="text-label">Twist Direction:</div>
                    <div class="text-content-half">
                        <p v-if="this.twistDirectionSingles">
                            Singles: {{ this.twistDirectionSingles }}
                        </p>
                        <p v-else>Singles: —</p>
                        <p v-if="this.twistDirectionPlied">
                            Plied: {{ this.twistDirectionPlied }}
                        </p>
                        <p v-else>Plied: —</p>
                    </div>
                </div>
                <div class="detail-text">
                    <div class="text-label">Twist Angle:</div>
                    <div class="text-content" v-if="this.twistAngle">
                        {{ this.twistAngle }} °
                    </div>
                    <div class="text-content" v-else>—</div>
                </div>
                <div class="detail-text">
                    <div class="text-label">Drive Ratios:</div>
                    <div class="text-content-half">
                        <p v-if="this.driveRatioSingles">
                            Singles: {{ this.driveRatioSingles }}
                        </p>
                        <p v-else>Singles: —</p>
                        <p v-if="this.driveRatioPlied">
                            Plied: {{ this.driveRatioPlied }}
                        </p>
                        <p v-else>Plied: —</p>
                    </div>
                </div>

                <div class="divider" />
            </span>
            <!-- WEAVING -->
            <span v-if="this.craftTypes?.includes('weaving')">
                <div class="detail-text">
                    <div class="text-label">Warp Yarn:</div>
                    <div class="text-content" v-if="this.warpYarn">
                        {{ this.warpYarn }}
                    </div>
                    <div v-else>—</div>
                </div>
                <div class="detail-text">
                    <div class="text-label">Weft Yarn:</div>
                    <div class="text-content" v-if="this.weftYarn">
                        {{ this.weftYarn }}
                    </div>
                    <div v-else>—</div>
                </div>
                <div class="detail-text">
                    <div class="text-label">EPI x PPI:</div>
                    <div class="text-content" v-if="this.epi && this.ppi">
                        {{ this.epi }} EPI x {{ this.ppi }} PPI
                    </div>
                    <div class="text-content" v-else-if="this.epi">
                        {{ this.epi }} EPI
                    </div>
                    <div class="text-content" v-else-if="this.ppi">
                        {{ this.ppi }} PPI
                    </div>
                    <div class="text-content" v-else>—</div>
                </div>
                <div class="detail-text">
                    <div class="text-label">Total Ends:</div>
                    <div class="text-content" v-if="this.totalEnds">
                        {{ this.totalEnds }}
                    </div>
                    <div class="text-content" v-else>—</div>
                </div>
                <div class="detail-text">
                    <div class="text-label">Draft Notes:</div>
                    <div class="text-content" v-if="this.draftNotes">
                        {{ this.draftNotes }}
                    </div>
                    <div class="text-content" v-else>—</div>
                </div>
                <div class="detail-text">
                    <div class="text-label">Width in Reed:</div>
                    <div class="text-content" v-if="this.widthInReed">
                        {{ this.widthInReed }} {{ this.widthInReedUnit }}
                    </div>
                    <div class="text-content" v-else>—</div>
                </div>
                <div class="detail-text">
                    <div class="text-label">Warped Length:</div>
                    <div
                        class="text-content"
                        v-if="
                            this.warpedLength && this.warpedLengthUnit == 'yd'
                        "
                    >
                        {{ this.warpedLength }} yds
                    </div>
                    <div class="text-content" v-else-if="this.warpedLength">
                        {{ this.warpedLength }} {{ this.warpedLengthUnit }}
                    </div>
                    <div class="text-content" v-else>—</div>
                </div>
                <div class="detail-text">
                    <div class="text-label">Length Woven:</div>
                    <div
                        class="text-content"
                        v-if="this.length && this.lengthUnit == 'yd'"
                    >
                        {{ this.length }} yds
                    </div>
                    <div class="text-content" v-else-if="this.length">
                        {{ this.length }} {{ this.lengthUnit }}
                    </div>
                    <div class="text-content" v-else>—</div>
                </div>
                <div class="detail-text">
                    <div class="text-label">Finished Dimensions:</div>
                    <div
                        class="text-content"
                        v-if="this.finishedLength && this.finishedWidth"
                    >
                        {{ this.finishedLength }}
                        {{ this.finishedLengthUnit }} x
                        {{ this.finishedWidth }} {{ this.finishedWidthUnit }}
                    </div>
                    <div class="text-content" v-else-if="this.finishedLength">
                        {{ this.finishedLength }} {{ this.finishedLengthUnit }}
                    </div>
                    <div class="text-content" v-else-if="this.finishedWidth">
                        {{ this.finishedWidth }} {{ this.finishedWidthUnit }}
                    </div>
                    <div class="text-content" v-else>—</div>
                </div>

                <div class="divider" />
            </span>
            <!-- KNITTING -->
            <span v-if="this.craftTypes?.includes('knitting')">
                <div class="detail-text">
                    <div class="text-label">Size Made:</div>
                    <div class="text-content" v-if="this.sizeMade">
                        {{ this.sizeMade }}
                    </div>
                    <div class="text-content" v-else>—</div>
                </div>
                <div class="detail-text">
                    <div class="text-label">Needles Used:</div>
                    <div id="needles-container" v-if="this.needleSizes">
                        <p
                            class="attribute-container"
                            v-for="needleSize in this.needleSizes"
                            :key="needleSize"
                        >
                            {{ needleSize }}
                        </p>
                    </div>
                </div>
                <div class="detail-text">
                    <div class="text-label">Gauge:</div>
                    <div
                        id="gauge-container"
                        v-if="this.knitGaugeCount || this.knitGaugeRows"
                    >
                        <div id="gauge-container-row1">
                            <div v-if="this.knitGaugeUnit == 'sts'">
                                {{ knitGaugeCount }} stitches
                            </div>
                            <div v-else-if="this.knitGaugeUnit == 'reps'">
                                {{ knitGaugeCount }} repeats
                            </div>
                            <div v-else>—</div>
                            <p v-if="this.knitGaugeUnit && this.knitGaugeRows">
                                and
                            </p>
                            <div v-if="this.knitGaugeRows">
                                {{ knitGaugeRows }} rows
                            </div>
                            <div v-else>—</div>
                            <p v-if="this.knitGaugeCount || this.knitGaugeRows">
                                /
                            </p>
                        </div>
                        <div id="gauge-container-row2">
                            <div v-if="this.knitGaugeSizeUnit == 'in'">
                                {{ knitGaugeSizeWidth }} x
                                {{ knitGaugeSizeHeight }} inches
                            </div>
                            <div v-if="this.knitGaugeSizeUnit == 'cm'">
                                {{ knitGaugeSizeWidth }} x
                                {{ knitGaugeSizeHeight }} cm
                            </div>
                        </div>
                    </div>
                    <div id="gauge-container" v-else>—</div>
                </div>
                <div class="divider" />
            </span>
            <!-- CROCHETING -->
            <span v-if="this.craftTypes?.includes('crocheting')">
                <div
                    class="detail-text"
                    v-if="!this.craftTypes?.includes('knitting')"
                >
                    <div class="text-label">Size Made:</div>
                    <div class="text-content" v-if="this.sizeMade">
                        {{ this.sizeMade }}
                    </div>
                    <div class="text-content" v-else>—</div>
                </div>
                <div class="detail-text">
                    <div class="text-label">Hooks Used:</div>
                    <div id="hooks-container" v-if="this.hookSizes">
                        <p
                            class="attribute-container"
                            v-for="hookSize in this.hookSizes"
                            :key="hookSize"
                        >
                            {{ hookSizeChart[hookSize] }}
                        </p>
                    </div>
                    <div class="text-content" v-else>—</div>
                </div>
                <div class="detail-text">
                    <div class="text-label">Gauge:</div>
                    <div
                        id="gauge-container"
                        v-if="this.crochetGaugeCount || this.crochetGaugeRows"
                    >
                        <div id="gauge-container-row1">
                            <div v-if="this.crochetGaugeUnit == 'sts'">
                                {{ crochetGaugeCount }} stitches
                            </div>
                            <div v-else-if="this.crochetGaugeUnit == 'reps'">
                                {{ crochetGaugeCount }} repeats
                            </div>
                            <div v-else>—</div>
                            <p
                                v-if="
                                    this.crochetGaugeUnit &&
                                    this.crochetGaugeRows
                                "
                            >
                                and
                            </p>
                            <div v-if="this.crochetGaugeRows">
                                {{ crochetGaugeRows }} rows
                            </div>
                            <div v-else>—</div>
                            <p
                                v-if="
                                    this.crochetGaugeCount ||
                                    this.crochetGaugeRows
                                "
                            >
                                /
                            </p>
                        </div>
                        <div id="gauge-container-row2">
                            <div v-if="this.crochetGaugeSizeUnit == 'in'">
                                {{ crochetGaugeSizeWidth }} x
                                {{ crochetGaugeSizeHeight }} inches
                            </div>
                            <div v-if="this.crochetGaugeSizeUnit == 'cm'">
                                {{ crochetGaugeSizeWidth }} x
                                {{ crochetGaugeSizeHeight }} cm
                            </div>
                        </div>
                    </div>
                    <div id="gauge-container" v-else>—</div>
                </div>
                <div class="divider" />
            </span>
            <!-- SEWING -->
            <span v-if="this.craftTypes?.includes('sewing')">
                <div
                    class="detail-text"
                    v-if="
                        !(
                            this.craftTypes?.includes('knitting') ||
                            this.craftTypes?.includes('crocheting')
                        )
                    "
                >
                    <div class="text-label">Size Made:</div>
                    <div class="text-content" v-if="this.sizeMade">
                        {{ this.sizeMade }}
                    </div>
                    <div class="text-content" v-else>—</div>
                </div>
                <div class="divider" />
            </span>
            <!-- EMBROIDERY -->
            <!-- LINKED GALLERY -->
            <div class="detail-text">
                <div class="text-label">Linked Materials:</div>
                <div
                    class="linked-gallery"
                    v-if="this.projectMaterials?.length"
                >
                    <div
                        class="linked-item"
                        v-for="material in this.projectMaterials"
                        :key="material.id"
                    >
                        <img
                            class="linked-image"
                            v-if="material.stashItem?.stashItemImages?.length"
                            :src="
                                material.stashItem.stashItemImages[0].imageURL
                            "
                            alt="User-uploaded image of material"
                            @click.prevent="
                                redirectStash(material.stashItem?.id)
                            "
                        />
                        <img
                            class="linked-image"
                            v-else
                            src="https://knotelry.s3.amazonaws.com/image-placeholder.png"
                            alt="No image found"
                            @click.prevent="
                                redirectStash(material.stashItem?.id)
                            "
                        />
                        <p
                            class="linked-link"
                            @click.prevent="
                                redirectStash(material.stashItem?.id)
                            "
                        >
                            {{ material.stashItem?.title }}
                        </p>
                        <p class="linked-p" v-if="material.fiberQuantityUsed">
                            {{ material.fiberQuantityUsed }}
                            {{ material.fiberQuantityUnit }} used
                        </p>
                        <p class="linked-p" v-else-if="material.lengthUsed">
                            {{ material.lengthUsed }}
                            {{ material.lengthUnit }} used
                        </p>
                        <p class="linked-p" v-else-if="material.skeinsUsed">
                            {{ material.skeinsUsed }} skeins used
                        </p>
                    </div>
                </div>
                <div class="text-content" v-else>—</div>
            </div>
            <div class="detail-text">
                <div class="text-label">Linked Tools:</div>
                <div class="linked-gallery" v-if="this.projectTools?.length">
                    <div
                        class="linked-item"
                        v-for="tool in this.projectTools"
                        :key="tool.id"
                    >
                        <img
                            class="linked-image"
                            v-if="tool.toolItem?.imageURL"
                            :src="tool.toolItem?.imageURL"
                            alt="User-uploaded image of tool"
                            @click.prevent="redirectTool(tool.toolItem?.id)"
                        />
                        <img
                            class="linked-image"
                            v-else
                            src="https://knotelry.s3.amazonaws.com/image-placeholder.png"
                            alt="No image found"
                            @click.prevent="redirectTool(tool.toolItem?.id)"
                        />
                        <p
                            class="linked-link"
                            @click.prevent="redirectStash(tool.toolItem?.id)"
                        >
                            {{ tool.toolItem?.title }}
                        </p>
                    </div>
                </div>
                <div class="text-content" v-else>—</div>
            </div>
            <!-- NOTES FIELD -->
            <div class="detail-text">
                <div class="text-label">Notes:</div>
                <div class="text-content" v-if="this.notes">
                    {{ this.notes }}
                </div>
                <div class="text-content" v-else>—</div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "ProjectDetail",
    mounted() {
        const data = loadProject(parseInt(this.$route.params.projectId)).then(
            (data) => {
                if (data) {
                    this.title = data.title;
                    this.description = data.description;
                    if (data.craftTypes.length) {
                        this.craftTypes = data.craftTypes?.split(" ");
                    }
                    this.patternName = data.patternName;
                    this.patternAuthor = data.patternAuthor;
                    this.linkToPattern = data.linkToPattern;
                    this.sizeMade = data.sizeMade;
                    this.tags = data.tags?.split(",");
                    this.status = data.status;
                    this.attributes = data.attributes?.split(",");
                    this.storedIn = data.storedIn;
                    this.startDate = data.startDate;
                    this.endDate = data.endDate;

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
                    this.finishedYarnLength = data.finishedYarnLength;
                    this.finishedYarnLengthUnit = data.finishedYarnLengthUnit;
                    this.finishedYarnWeight = data.finishedYarnWeight;
                    this.finishedYarnWeightUnit = data.finishedYarnWeightUnit;

                    this.warpYarn = data.warpYarn;
                    this.weftYarn = data.weftYarn;
                    this.epi = data.epi;
                    this.ppi = data.ppi;
                    this.totalEnds = data.totalEnds;
                    this.draftNotes = data.draftNotes;

                    this.widthInReed = data.widthInReed;
                    this.widthInReedUnit = data.widthInReedUnit;
                    this.warpedLength = data.warpedLength;
                    this.warpedLengthUnit = data.warpedLengthUnit;
                    this.length = data.length;
                    this.lengthUnit = data.lengthUnit;
                    this.finishedLength = data.finishedLength;
                    this.finishedLengthUnit = data.finishedLengthUnit;
                    this.finishedWidth = data.finishedWidth;
                    this.finishedWidthUnit = data.finishedWidthUnit;

                    this.needleSizes = data.needleSizes?.split(",");
                    this.knitGaugeCount = data.knitGaugeCount;
                    this.knitGaugeUnit = data.knitGaugeUnit;
                    this.knitGaugeRows = data.knitGaugeRows;
                    this.knitGaugeSizeWidth = data.knitGaugeSizeWidth;
                    this.knitGaugeSizeHeight = data.knitGaugeSizeHeight;
                    this.knitGaugeSizeUnit = data.knitGaugeSizeUnit;

                    this.hookSizes = data.hookSizes?.split(",");
                    this.crochetGaugeCount = data.crochetGaugeCount;
                    this.crochetGaugeUnit = data.crochetGaugeUnit;
                    this.crochetGaugeRows = data.crochetGaugeRows;
                    this.crochetGaugeSizeWidth = data.crochetGaugeSizeWidth;
                    this.crochetGaugeSizeHeight = data.crochetGaugeSizeHeight;
                    this.crochetGaugeSizeUnit = data.crochetGaugeSizeUnit;

                    this.notes = data.notes;
                    this.createdAt = data.createdAt;
                    this.updatedAt = data.updatedAt;

                    this.user = data.user;
                    this.projectMaterials = data.projectMaterials;
                    this.projectTools = data.projectTools;
                    this.projectImages = data.projectImages;
                } else {
                    this.$router.push("/404");
                }
            }
        );
    },
    data() {
        return {
            title: null,
            description: null,
            craftTypes: null,
            patternName: null,
            patternAuthor: null,
            linkToPattern: null,
            sizeMade: null,
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
            finishedYarnLength: null,
            finishedYarnLengthUnit: null,
            finishedYarnWeight: null,
            finishedYarnWeightUnit: null,

            warpYarn: null,
            weftYarn: null,
            epi: null,
            ppi: null,
            totalEnds: null,
            draftNotes: null,

            widthInReed: null,
            widthInReedUnit: null,
            warpedLength: null,
            warpedLengthUnit: null,
            length: null,
            lengthUnit: null,
            finishedLength: null,
            finishedLengthUnit: null,
            finishedWidth: null,
            finishedWidthUnit: null,

            needleSizes: null,
            knittingSizeChart: {
                1.5: "000 (1.5 mm)",
                1.75: "00 (1.75 mm)",
                2: "0 (2 mm)",
                2.25: "1 (2.25 mm)",
                2.75: "2 (2.75 mm)",
                3: "3 mm",
                3.25: "3 (3.25 mm)",
                3.5: "4 (3.5 mm)",
                3.75: "5 (3.75 mm)",
                4: "6 (4 mm)",
                4.5: "7 (4.5 mm)",
                5: "8 (5 mm)",
                5.5: "9 (5.5 mm)",
                6: "10 (6 mm)",
                6.5: "10 1/2 (6.5 mm)",
                7: "7 mm",
                8: "11 (8 mm)",
                9: "13 (9 mm)",
                10: "15 (10 mm)",
                12.5: "17 (12.5 mm)",
                15: "19 (15 mm)",
                19: "35 (19 mm)",
                25: "50 (25 mm)",
                35: "70 (35 mm)",
            },
            knitGaugeCount: null,
            knitGaugeUnit: null,
            knitGaugeRows: null,
            knitGaugeSizeWidth: null,
            knitGaugeSizeHeight: null,
            knitGaugeSizeUnit: null,

            hookSizes: null,
            hookSizeChart: {
                2.25: "B-1 (2.25 mm)",
                2.75: "C-2 (2.75 mm)",
                3.125: "D (3.125 mm)",
                3.25: "D-3 (3.25 mm)",
                3.5: "E-4 (3.5 mm)",
                3.75: "F-5 (3.75 mm)",
                4: "G-6 (4 mm)",
                4.25: "G (4.25 mm)",
                4.5: "7 (4.5 mm)",
                5: "H-8 (5 mm)",
                5.25: "I (5.25 mm)",
                5.5: "J (5.5 mm)",
                6: "J-10 (6 mm)",
                6.5: "K-10 1/2 (6.5 mm)",
                8: "L-11 (8 mm)",
                9: "M/N-13 (9 mm)",
                10: "N/P-15 (10 mm)",
                11.5: "P-16 (11.5 mm)",
                15: "P/Q (15 mm)",
                16: "Q (16 mm)",
                19: "S (19 mm)",
                25: "T/U/X (25 mm)",
                30: "T/X (30 mm)",
            },
            crochetGaugeCount: null,
            crochetGaugeUnit: null,
            crochetGaugeRows: null,
            crochetGaugeSizeWidth: null,
            crochetGaugeSizeHeight: null,
            crochetGaugeSizeUnit: null,

            notes: null,
            createdAt: null,
            updatedAt: null,

            user: null,
            projectMaterials: [],
            projectTools: [],
            projectImages: [],
        };
    },
    methods: {
        redirectStash: function (id) {
            this.$router.push(`/stash/${id}`);
        },
        redirectTool: function (id) {
            this.$router.push(`/tools/${id}`);
        },
        editProject: function (id) {
            this.$router.push(`/projects/${this.$route.params.projectId}/edit`);
        },
        deleteProject: function (id) {
            this.$router.push(
                `/projects/${this.$route.params.projectId}/delete`
            );
        },
    },
};

const loadProject = async (projectId) => {
    const response = await fetch(`/api/projects/${projectId}`);
    if (response.ok) {
        const data = await response.json();
        return data;
    } else {
        const data = false;
        return false;
    }
};

const loadLinkedMaterials = async (projectId) => {
    const response = await fetch(`/api/projects/${projectId}/materials`);
    if (response.ok) {
        const materialsData = await response.json();
        return materialsData;
    } else {
        return false;
    }
};
</script>

<style scoped>
p {
    margin-top: 0px;
    margin-bottom: 0px;
}
a {
    text-decoration: none;
    color: var(--color-shadow);
    font-weight: bold;
}

.project-detail {
    display: grid;
    grid-template-columns: 250px 1fr;
    column-gap: 100px;
    padding-left: 14%;
    padding-right: 14%;
    padding-top: 60px;
}

.left {
    display: flex;
    flex-direction: column;
    padding-bottom: 32px;
}

.detail-image {
    margin-left: auto;
    margin-right: auto;
    margin-top: 8px;
    margin-bottom: 8px;
    width: 100%;
    object-fit: cover;
    border: 1px solid var(--color-shadow);
    border-radius: 6px;
}

.project-header {
    margin-left: auto;
    margin-right: auto;
    width: 250px;
    align-items: center;
    text-align: center;
}

.project-header > h2 {
    margin-top: 0px;
}

.project-options {
    width: 100%;
    display: grid;
    grid-template-columns: 1fr 1fr;
    margin-left: auto;
    margin-right: auto;
    column-gap: 4px;
    margin-bottom: 8px;
}

button {
    font-family: "Open Sans", sans-serif;
    letter-spacing: 1px;
    padding-top: 4px;
    padding-bottom: 4px;
    border-radius: 4px;
    border: 1px solid var(--color-shadow);
    box-shadow: 1px 1px 1px var(--color-shadow);
    background-color: var(--color-primary-contrast);
    color: white;
    font-size: 15px;
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

.text-content-half {
    display: grid;
    grid-template-columns: 1fr 1fr;
    column-gap: 8px;
}

.text-content-half > p {
    margin: 0px;
}

.attributes-container {
    display: grid;
    grid-template-columns: repeat(auto-fill, 130px);
    column-gap: 4px;
    row-gap: 4px;
}

.attribute-container {
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

#needles-container {
    display: grid;
    grid-template-columns: repeat(auto-fill, 75px);
    column-gap: 4px;
    row-gap: 4px;
}

#hooks-container {
    display: grid;
    grid-template-columns: repeat(auto-fill, 150px);
    column-gap: 4px;
    row-gap: 4px;
}

#gauge-container {
    display: flex;
    flex-direction: column;
}

#gauge-container-row1 {
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    column-gap: 4px;
}

.divider {
    border-top: 1px solid var(--color-shadow);
    margin-top: 16px;
    margin-bottom: 16px;
    padding: 0px;
}

.linked-gallery {
    display: grid;
    grid-template-columns: repeat(auto-fill, 100px);
    grid-gap: 12px;
    justify-content: space-between;
}

.linked-item {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.linked-image {
    width: 100px;
    height: 100px;
    object-fit: cover;
    border: 1px solid var(--color-shadow);
    border-radius: 4px;
}

.linked-image:hover {
    cursor: pointer;
}

.linked-link {
    margin-top: 0px;
    margin-bottom: 0px;
    text-align: center;
}

.linked-link:hover {
    font-weight: bold;
    cursor: pointer;
}

.linked-p {
    margin-top: 2px;
    font-size: 12px;
}

.text-label {
    text-align: justify;
    align-self: flex-start;
}
</style>
