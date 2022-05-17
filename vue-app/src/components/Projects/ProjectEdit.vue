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
                <label for="description" class="label-top-align"
                    >Description:</label
                >
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
                <div class="spacer" />
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
                            v-model="this.finishedYarnLength"
                        />
                        <select v-model="this.finishedYarnLengthUnit">
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
                            v-model="this.finishedYarnWeight"
                        />
                        <select v-model="this.finishedYarnWeightUnit">
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
                <div class="spacer" />
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
                    <label for="ppi">PPI (Picks Per Inch):</label>
                    <input
                        type="number"
                        step="0.01"
                        placeholder="0"
                        v-model="this.ppi"
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
                    <label for="draftNotes" class="label-top-align"
                        >Draft Notes:</label
                    >
                    <textarea
                        placeholder="Enter notes for your project's draft"
                        v-model="this.draftNotes"
                    />
                </div>

                <div class="form-element">
                    <label for="widthInReed">Width In Reed:</label>
                    <div class="input-select">
                        <input
                            type="number"
                            step="0.01"
                            placeholder="0"
                            v-model="this.widthInReed"
                        />
                        <select v-model="this.widthInReedUnit">
                            <option value="null" selected disabled hidden>
                                —
                            </option>
                            <option value="in">inches</option>
                            <option value="cm">centimeters</option>
                        </select>
                    </div>
                </div>
                <div class="form-element">
                    <label for="warpedLength">Warped Length:</label>
                    <div class="input-select">
                        <input
                            type="number"
                            step="0.01"
                            placeholder="0"
                            v-model="this.warpedLength"
                        />
                        <select v-model="this.warpedLengthUnit">
                            <option value="null" selected disabled hidden>
                                —
                            </option>
                            <option value="in">inches</option>
                            <option value="yd">yards</option>
                            <option value="cm">centimeters</option>
                            <option value="m">meters</option>
                        </select>
                    </div>
                </div>
                <div class="form-element">
                    <label for="length">Length Woven:</label>
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
                            <option value="yd">yards</option>
                            <option value="cm">centimeters</option>
                            <option value="m">meters</option>
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
                        <select v-model="this.finishedLengthUnit">
                            <option value="null" selected disabled hidden>
                                —
                            </option>
                            <option value="in">inches</option>
                            <option value="yd">yards</option>
                            <option value="cm">centimeters</option>
                            <option value="m">meters</option>
                        </select>
                    </div>
                </div>
                <div class="form-element">
                    <label for="finishedWidth">Finished Width:</label>
                    <div class="input-select">
                        <input
                            type="number"
                            step="0.01"
                            placeholder="0"
                            v-model="this.finishedWidth"
                        />
                        <select v-model="this.finishedWidthUnit">
                            <option value="null" selected disabled hidden>
                                —
                            </option>
                            <option value="in">inches</option>
                            <option value="yd">yards</option>
                            <option value="cm">centimeters</option>
                            <option value="m">meters</option>
                        </select>
                    </div>
                </div>
            </span>

            <!-- KNITTING -->
            <span v-if="this.knitting">
                <div class="spacer" />
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
                    <div id="needles-container">
                        <button
                            v-bind:class="{ selected: isKnitting01 }"
                            @click.prevent="
                                this.isKnitting01 = !this.isKnitting01
                            "
                        >
                            000 (1.5 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: isKnitting02 }"
                            @click.prevent="
                                this.isKnitting02 = !this.isKnitting02
                            "
                        >
                            00 (1.75 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: isKnitting03 }"
                            @click.prevent="
                                this.isKnitting03 = !this.isKnitting03
                            "
                        >
                            0 (2 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: isKnitting04 }"
                            @click.prevent="
                                this.isKnitting04 = !this.isKnitting04
                            "
                        >
                            1 (2.25 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: isKnitting05 }"
                            @click.prevent="
                                this.isKnitting05 = !this.isKnitting05
                            "
                        >
                            2 (2.75 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: isKnitting06 }"
                            @click.prevent="
                                this.isKnitting06 = !this.isKnitting06
                            "
                        >
                            3 mm
                        </button>
                        <button
                            v-bind:class="{ selected: isKnitting07 }"
                            @click.prevent="
                                this.isKnitting07 = !this.isKnitting07
                            "
                        >
                            3 (3.25 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: isKnitting08 }"
                            @click.prevent="
                                this.isKnitting08 = !this.isKnitting08
                            "
                        >
                            4 (3.5 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: isKnitting09 }"
                            @click.prevent="
                                this.isKnitting09 = !this.isKnitting09
                            "
                        >
                            5 (3.75 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: isKnitting10 }"
                            @click.prevent="
                                this.isKnitting10 = !this.isKnitting10
                            "
                        >
                            6 (4 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: isKnitting11 }"
                            @click.prevent="
                                this.isKnitting11 = !this.isKnitting11
                            "
                        >
                            7 (4.5 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: isKnitting12 }"
                            @click.prevent="
                                this.isKnitting12 = !this.isKnitting12
                            "
                        >
                            8 (5 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: isKnitting13 }"
                            @click.prevent="
                                this.isKnitting13 = !this.isKnitting13
                            "
                        >
                            9 (5.5 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: isKnitting14 }"
                            @click.prevent="
                                this.isKnitting14 = !this.isKnitting14
                            "
                        >
                            10 (6 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: isKnitting15 }"
                            @click.prevent="
                                this.isKnitting15 = !this.isKnitting15
                            "
                        >
                            10 1/2 (6.5 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: isKnitting16 }"
                            @click.prevent="
                                this.isKnitting16 = !this.isKnitting16
                            "
                        >
                            7 mm
                        </button>
                        <button
                            v-bind:class="{ selected: isKnitting17 }"
                            @click.prevent="
                                this.isKnitting17 = !this.isKnitting17
                            "
                        >
                            11 (8 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: isKnitting18 }"
                            @click.prevent="
                                this.isKnitting18 = !this.isKnitting18
                            "
                        >
                            13 (9 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: isKnitting19 }"
                            @click.prevent="
                                this.isKnitting19 = !this.isKnitting19
                            "
                        >
                            15 (10 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: isKnitting20 }"
                            @click.prevent="
                                this.isKnitting20 = !this.isKnitting20
                            "
                        >
                            17 (12.5 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: isKnitting21 }"
                            @click.prevent="
                                this.isKnitting21 = !this.isKnitting21
                            "
                        >
                            19 (15 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: isKnitting22 }"
                            @click.prevent="
                                this.isKnitting22 = !this.isKnitting22
                            "
                        >
                            35 (19 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: isKnitting23 }"
                            @click.prevent="
                                this.isKnitting23 = !this.isKnitting23
                            "
                        >
                            50 (25 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: isKnitting24 }"
                            @click.prevent="
                                this.isKnitting24 = !this.isKnitting24
                            "
                        >
                            70 (35 mm)
                        </button>
                    </div>
                </div>
                <div class="form-element">
                    <label for="gauge" class="label-top-align">Gauge:</label>
                    <div id="gauge-container">
                        <div id="gauge-container-row1">
                            <input
                                type="number"
                                placeholder="0"
                                v-model="this.knitGaugeCount"
                            />
                            <select v-model="this.knitGaugeUnit">
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
                                v-model="this.knitGaugeRows"
                            />
                            <p>rows/rounds</p>
                        </div>
                        <div id="gauge-container-row2">
                            <p>/</p>
                            <input
                                type="number"
                                placeholder="0"
                                v-model="this.knitGaugeSizeWidth"
                            />
                            <p>x</p>
                            <input
                                type="number"
                                placeholder="0"
                                v-model="this.knitGaugeSizeHeight"
                            />
                            <select v-model="this.knitGaugeSizeUnit">
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
                <div class="spacer" />
                <div class="form-element" v-if="!this.knitting">
                    <label for="sizeMade">Size Made:</label>
                    <input
                        type="text"
                        placeholder="Enter size information"
                        v-model="this.sizeMade"
                    />
                </div>
                <div class="form-element">
                    <label for="hooks" class="label-top-align"
                        >Hooks Used:</label
                    >
                    <div id="hooks-container">
                        <button
                            v-bind:class="{ selected: isHook01 }"
                            @click.prevent="this.isHook01 = !this.isHook01"
                        >
                            B-1 (2.25 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: isHook02 }"
                            @click.prevent="this.isHook02 = !this.isHook02"
                        >
                            2.5mm
                        </button>
                        <button
                            v-bind:class="{ selected: isHook03 }"
                            @click.prevent="this.isHook03 = !this.isHook03"
                        >
                            C-2 (2.75 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: isHook04 }"
                            @click.prevent="this.isHook04 = !this.isHook04"
                        >
                            D (3.125 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: isHook05 }"
                            @click.prevent="this.isHook05 = !this.isHook05"
                        >
                            D-3 (3.25 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: isHook06 }"
                            @click.prevent="this.isHook06 = !this.isHook06"
                        >
                            E-4 (3.5 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: isHook07 }"
                            @click.prevent="this.isHook07 = !this.isHook07"
                        >
                            F-5 (3.75 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: isHook08 }"
                            @click.prevent="this.isHook08 = !this.isHook08"
                        >
                            G-6 (4 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: isHook09 }"
                            @click.prevent="this.isHook09 = !this.isHook09"
                        >
                            G (4.25 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: isHook10 }"
                            @click.prevent="this.isHook10 = !this.isHook10"
                        >
                            7 (4.5 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: isHook11 }"
                            @click.prevent="this.isHook11 = !this.isHook11"
                        >
                            H-8 (5 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: isHook12 }"
                            @click.prevent="this.isHook12 = !this.isHook12"
                        >
                            I (5.25 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: isHook13 }"
                            @click.prevent="this.isHook13 = !this.isHook13"
                        >
                            J (5.5 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: isHook14 }"
                            @click.prevent="this.isHook14 = !this.isHook14"
                        >
                            J-10 (6 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: isHook15 }"
                            @click.prevent="this.isHook15 = !this.isHook15"
                        >
                            K-10 1/2 (6.5 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: isHook16 }"
                            @click.prevent="this.isHook16 = !this.isHook16"
                        >
                            L-11 (8 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: isHook17 }"
                            @click.prevent="this.isHook17 = !this.isHook17"
                        >
                            M/N-13 (9 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: isHook18 }"
                            @click.prevent="this.isHook18 = !this.isHook18"
                        >
                            N/P-15 (10 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: isHook19 }"
                            @click.prevent="this.isHook19 = !this.isHook19"
                        >
                            P-16 (11.5 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: isHook20 }"
                            @click.prevent="this.isHook20 = !this.isHook20"
                        >
                            P/Q (15 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: isHook21 }"
                            @click.prevent="this.isHook21 = !this.isHook21"
                        >
                            Q (16 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: isHook22 }"
                            @click.prevent="this.isHook22 = !this.isHook22"
                        >
                            S (19 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: isHook23 }"
                            @click.prevent="this.isHook23 = !this.isHook23"
                        >
                            T/U/X (25 mm)
                        </button>
                        <button
                            v-bind:class="{ selected: isHook24 }"
                            @click.prevent="this.isHook24 = !this.isHook24"
                        >
                            T/X (30 mm)
                        </button>
                    </div>
                </div>
                <div class="form-element">
                    <label for="gauge" class="label-top-align">Gauge:</label>
                    <div id="gauge-container">
                        <div id="gauge-container-row1">
                            <input
                                type="number"
                                placeholder="0"
                                v-model="this.crochetGaugeCount"
                            />
                            <select v-model="this.crochetGaugeUnit">
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
                                v-model="this.crochetGaugeRows"
                            />
                            <p>rows/rounds</p>
                        </div>
                        <div id="gauge-container-row2">
                            <p>/</p>
                            <input
                                type="number"
                                placeholder="0"
                                v-model="this.crochetGaugeSizeWidth"
                            />
                            <p>x</p>
                            <input
                                type="number"
                                placeholder="0"
                                v-model="this.crochetGaugeSizeHeight"
                            />
                            <select v-model="this.crochetGaugeSizeUnit">
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

            <!-- SEWING -->
            <span v-if="this.sewing && !this.knitting && !this.crocheting">
                <div class="spacer" />
                <div class="form-element">
                    <label for="sizeMade">Size Made:</label>
                    <input
                        type="text"
                        placeholder="Enter size information"
                        v-model="this.sizeMade"
                    />
                </div>
            </span>

            <div class="spacer" />
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
                                            v-else-if="
                                                materialLink.stashItem.type ==
                                                'yarn'
                                            "
                                        >
                                            {{ materialLink.lengthUsed }}
                                            {{ materialLink.lengthUnit }} used
                                        </p>
                                        <p
                                            v-else-if="
                                                materialLink.stashItem.type ==
                                                'fabric'
                                            "
                                        >
                                            {{ materialLink.lengthUsed }}
                                            {{ materialLink.lengthUnit }} used
                                        </p>
                                        <p
                                            v-else-if="
                                                materialLink.stashItem.type ==
                                                'thread'
                                            "
                                        >
                                            {{ materialLink.lengthUsed }}
                                            {{ materialLink.lengthUnit }} used
                                        </p>
                                        <p
                                            v-else-if="
                                                materialLink.stashItem.type ==
                                                    'aida' &&
                                                materialLink.unitsUsed == 1
                                            "
                                        >
                                            {{ materialLink.unitsUsed }} unit
                                            used
                                        </p>
                                        <p
                                            v-else-if="
                                                materialLink.stashItem.type ==
                                                'aida'
                                            "
                                        >
                                            {{ materialLink.unitsUsed }} units
                                            used
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

            isKnitting01: false,
            isKnitting02: false,
            isKnitting03: false,
            isKnitting04: false,
            isKnitting05: false,
            isKnitting06: false,
            isKnitting07: false,
            isKnitting08: false,
            isKnitting09: false,
            isKnitting10: false,
            isKnitting11: false,
            isKnitting12: false,
            isKnitting13: false,
            isKnitting14: false,
            isKnitting15: false,
            isKnitting16: false,
            isKnitting17: false,
            isKnitting18: false,
            isKnitting19: false,
            isKnitting20: false,
            isKnitting21: false,
            isKnitting22: false,
            isKnitting23: false,
            isKnitting24: false,

            knitGaugeCount: null,
            knitGaugeUnit: null,
            knitGaugeRows: null,
            knitGaugeSizeWidth: null,
            knitGaugeSizeHeight: null,
            knitGaugeSizeUnit: null,

            hookSizes: null,

            isHook01: false,
            isHook02: false,
            isHook03: false,
            isHook04: false,
            isHook05: false,
            isHook06: false,
            isHook07: false,
            isHook08: false,
            isHook09: false,
            isHook10: false,
            isHook11: false,
            isHook12: false,
            isHook13: false,
            isHook14: false,
            isHook15: false,
            isHook16: false,
            isHook17: false,
            isHook18: false,
            isHook19: false,
            isHook20: false,
            isHook21: false,
            isHook22: false,
            isHook23: false,
            isHook24: false,

            crochetGaugeCount: null,
            crochetGaugeUnit: null,
            crochetGaugeRows: null,
            crochetGaugeSizeWidth: null,
            crochetGaugeSizeHeight: null,
            crochetGaugeSizeUnit: null,

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

                this.needleSizes = data.needleSizes;

                const knittingNeedlesArr = this.needleSizes?.split(",");
                this.isKnitting01 = knittingNeedlesArr?.includes("1.5");
                this.isKnitting02 = knittingNeedlesArr?.includes("1.75");
                this.isKnitting03 = knittingNeedlesArr?.includes("2");
                this.isKnitting04 = knittingNeedlesArr?.includes("2.25");
                this.isKnitting05 = knittingNeedlesArr?.includes("2.75");
                this.isKnitting06 = knittingNeedlesArr?.includes("3");
                this.isKnitting07 = knittingNeedlesArr?.includes("3.25");
                this.isKnitting08 = knittingNeedlesArr?.includes("3.5");
                this.isKnitting09 = knittingNeedlesArr?.includes("3.75");
                this.isKnitting10 = knittingNeedlesArr?.includes("4");
                this.isKnitting11 = knittingNeedlesArr?.includes("4.5");
                this.isKnitting12 = knittingNeedlesArr?.includes("5");
                this.isKnitting13 = knittingNeedlesArr?.includes("5.5");
                this.isKnitting14 = knittingNeedlesArr?.includes("6");
                this.isKnitting15 = knittingNeedlesArr?.includes("6.5");
                this.isKnitting16 = knittingNeedlesArr?.includes("7");
                this.isKnitting17 = knittingNeedlesArr?.includes("8");
                this.isKnitting18 = knittingNeedlesArr?.includes("9");
                this.isKnitting19 = knittingNeedlesArr?.includes("10");
                this.isKnitting20 = knittingNeedlesArr?.includes("12.5");
                this.isKnitting21 = knittingNeedlesArr?.includes("15");
                this.isKnitting22 = knittingNeedlesArr?.includes("19");
                this.isKnitting23 = knittingNeedlesArr?.includes("25");
                this.isKnitting24 = knittingNeedlesArr?.includes("35");

                this.knitGaugeCount = data.knitGaugeCount;
                this.knitGaugeUnit = data.knitGaugeUnit;
                this.knitGaugeRows = data.knitGaugeRows;
                this.knitGaugeSizeWidth = data.knitGaugeSizeWidth;
                this.knitGaugeSizeHeight = data.knitGaugeSizeHeight;
                this.knitGaugeSizeUnit = data.knitGaugeSizeUnit;

                this.hookSizes = data.hookSizes;

                const hooksArr = this.hookSizes?.split(",");
                this.isHook01 = hooksArr?.includes("2.25");
                this.isHook02 = hooksArr?.includes("2.5");
                this.isHook03 = hooksArr?.includes("2.75");
                this.isHook04 = hooksArr?.includes("3.125");
                this.isHook05 = hooksArr?.includes("3.25");
                this.isHook06 = hooksArr?.includes("3.5");
                this.isHook07 = hooksArr?.includes("3.75");
                this.isHook08 = hooksArr?.includes("4");
                this.isHook09 = hooksArr?.includes("4.25");
                this.isHook10 = hooksArr?.includes("4.5");
                this.isHook11 = hooksArr?.includes("5");
                this.isHook12 = hooksArr?.includes("5.25");
                this.isHook13 = hooksArr?.includes("5.5");
                this.isHook14 = hooksArr?.includes("6");
                this.isHook15 = hooksArr?.includes("6.5");
                this.isHook16 = hooksArr?.includes("8");
                this.isHook17 = hooksArr?.includes("9");
                this.isHook18 = hooksArr?.includes("10");
                this.isHook19 = hooksArr?.includes("11.5");
                this.isHook20 = hooksArr?.includes("15");
                this.isHook21 = hooksArr?.includes("16");
                this.isHook22 = hooksArr?.includes("19");
                this.isHook23 = hooksArr?.includes("25");
                this.isHook24 = hooksArr?.includes("30");

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

                let knittingNeedles = "";

                if (this.isKnitting01) knittingNeedles += "1.5,";
                if (this.isKnitting02) knittingNeedles += "1.75,";
                if (this.isKnitting03) knittingNeedles += "2,";
                if (this.isKnitting04) knittingNeedles += "2.25,";
                if (this.isKnitting05) knittingNeedles += "2.75,";
                if (this.isKnitting06) knittingNeedles += "3,";
                if (this.isKnitting07) knittingNeedles += "3.25,";
                if (this.isKnitting08) knittingNeedles += "3.5,";
                if (this.isKnitting09) knittingNeedles += "3.75,";
                if (this.isKnitting10) knittingNeedles += "4,";
                if (this.isKnitting11) knittingNeedles += "4.5,";
                if (this.isKnitting12) knittingNeedles += "5,";
                if (this.isKnitting13) knittingNeedles += "5.5,";
                if (this.isKnitting14) knittingNeedles += "6,";
                if (this.isKnitting15) knittingNeedles += "6.5,";
                if (this.isKnitting16) knittingNeedles += "7,";
                if (this.isKnitting17) knittingNeedles += "8,";
                if (this.isKnitting18) knittingNeedles += "9,";
                if (this.isKnitting19) knittingNeedles += "10,";
                if (this.isKnitting20) knittingNeedles += "12.5,";
                if (this.isKnitting21) knittingNeedles += "15,";
                if (this.isKnitting22) knittingNeedles += "19,";
                if (this.isKnitting23) knittingNeedles += "25,";
                if (this.isKnitting24) knittingNeedles += "35,";

                if (knittingNeedles?.length) {
                    knittingNeedles = knittingNeedles.slice(0, -1);
                } else {
                    knittingNeedles = null;
                }

                let hooks = "";

                if (this.isHook01) hooks += "2.25,";
                if (this.isHook02) hooks += "2.5,";
                if (this.isHook03) hooks += "2.75,";
                if (this.isHook04) hooks += "3.125,";
                if (this.isHook05) hooks += "3.25,";
                if (this.isHook06) hooks += "3.5,";
                if (this.isHook07) hooks += "3.75,";
                if (this.isHook08) hooks += "4,";
                if (this.isHook09) hooks += "4.25,";
                if (this.isHook10) hooks += "4.5,";
                if (this.isHook11) hooks += "5,";
                if (this.isHook12) hooks += "5.25,";
                if (this.isHook13) hooks += "5.5,";
                if (this.isHook14) hooks += "6,";
                if (this.isHook15) hooks += "6.5,";
                if (this.isHook16) hooks += "8,";
                if (this.isHook17) hooks += "9,";
                if (this.isHook18) hooks += "10,";
                if (this.isHook19) hooks += "11.5,";
                if (this.isHook20) hooks += "15,";
                if (this.isHook21) hooks += "16,";
                if (this.isHook22) hooks += "19,";
                if (this.isHook23) hooks += "25,";
                if (this.isHook24) hooks += "30,";

                if (hooks?.length) {
                    hooks = hooks.slice(0, -1);
                } else {
                    hooks = null;
                }

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
                    finished_yarn_length: this.finishedYarnLength,
                    finished_yarn_length_unit: this.finishedYarnLengthUnit,
                    finished_yarn_weight: this.finishedYarnWeight,
                    finished_yarn_weight_unit: this.finishedYarnWeightUnit,

                    warp_yarn: this.warpYarn,
                    weft_yarn: this.weftYarn,
                    epi: this.epi,
                    ppi: this.ppi,
                    total_ends: this.totalEnds,
                    draft_notes: this.draftNotes,

                    width_in_reed: this.widthInReed,
                    width_in_reed_unit: this.widthInReedUnit,
                    warped_length: this.warpedLength,
                    warped_length_unit: this.warpedLengthUnit,
                    length: this.length,
                    length_unit: this.lengthUnit,
                    finished_length: this.finishedLength,
                    finished_length_unit: this.finishedLengthUnit,
                    finished_width: this.finishedWidth,
                    finished_width_unit: this.finishedWidthUnit,

                    needle_sizes: knittingNeedles,
                    knit_gauge_count: this.knitGaugeCount,
                    knit_gauge_unit: this.knitGaugeUnit,
                    knit_gauge_rows: this.knitGaugeRows,
                    knit_gauge_size_width: this.knitGaugeSizeWidth,
                    knit_gauge_size_height: this.knitGaugeSizeHeight,
                    knit_gauge_size_unit: this.knitGaugeSizeUnit,

                    hook_sizes: hooks,
                    crochet_gauge_count: this.crochetGaugeCount,
                    crochet_gauge_unit: this.crochetGaugeUnit,
                    crochet_gauge_rows: this.crochetGaugeRows,
                    crochet_gauge_size_width: this.crochetGaugeSizeWidth,
                    crochet_gauge_size_height: this.crochetGaugeSizeHeight,
                    crochet_gauge_size_unit: this.crochetGaugeSizeUnit,

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
    align-self: flex-start;
    margin-top: 4px;
}

.label-top-align {
    align-self: flex-start;
    margin-top: 8px;
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
    column-gap: 8px;
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

#needles-container {
    display: grid;
    grid-template-columns: repeat(auto-fill, 150px);
    column-gap: 4px;
    row-gap: 4px;
    margin-top: 8px;
    margin-bottom: 8px;
}

#hooks-container {
    display: grid;
    grid-template-columns: repeat(auto-fill, 150px);
    column-gap: 4px;
    row-gap: 4px;
    margin-top: 8px;
    margin-bottom: 8px;
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

.spacer {
    height: 28px;
}

.link:hover {
    font-weight: bold;
    cursor: pointer;
}

.input-select {
    display: grid;
    grid-template-columns: 1fr 1fr;
    width: 100%;
    column-gap: 16px;
}

.input-select > p {
    align-self: center;
    margin-top: 0px;
    margin-bottom: 0px;
}
</style>
