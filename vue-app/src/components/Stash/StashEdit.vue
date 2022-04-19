<template>
    <div class="stash-form-body">
        <div class="left">
            <div
                class="image-container"
                v-for="image in this.stashImages"
                :key="image.id"
            >
                <img
                    class="stash-image"
                    :src="image.imageURL"
                    alt="User uploaded image of stash"
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
            <p v-if="!this.stashImages || this.stashImages?.length == 0">
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
        <form class="stash-form" @submit.prevent="submit">
            <div class="form-element">
                <div />
                <h2>Editing Stash Item</h2>
            </div>
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
            <!-- STASH ITEM METADATA -->
            <div class="form-element">
                <label for="title">Title:</label>
                <input
                    type="text"
                    placeholder="Enter a title for your stash item"
                    v-model="title"
                />
            </div>
            <div class="form-element">
                <label for="Type">Type:</label>
                <select v-model="type">
                    <option value="null" selected disabled hidden>—</option>
                    <option value="fiber">Fiber</option>
                    <option value="yarn">Yarn</option>
                </select>
            </div>
            <div class="form-element" v-if="this.imageURL.length > 0">
                <div />
                <img
                    class="stash-image"
                    :src="this.imageURL"
                    alt="User uploaded image"
                />
            </div>
            <div class="form-element">
                <label for="status">Status:</label>
                <select v-model="status">
                    <option value="null" selected disabled hidden>—</option>
                    <option value="inStash">In Stash</option>
                    <option value="inUse">In Use</option>
                    <option value="usedUp">Used Up</option>
                    <option value="traded">Traded</option>
                    <option value="gifted">Gifted</option>
                </select>
            </div>
            <!-- ACQUIRED -->
            <div class="form-element">
                <label for="acquired">Date Acquired:</label>
                <input type="date" v-model="acquired" />
            </div>
            <div class="form-element">
                <label for="acquiredFrom">Acquired From:</label>
                <input
                    type="text"
                    placeholder="From where did you get this stash item?"
                    v-model="acquiredFrom"
                />
            </div>
            <div class="form-element">
                <label for="acquiredPrice">Price:</label>
                <div class="input-select">
                    <input
                        type="text"
                        placeholder="How much did you pay for this stash item?"
                        v-model="acquiredPrice"
                    />
                    <select v-model="acquiredCurrency">
                        <option value="null" selected disabled hidden>
                            currency
                        </option>
                        <option value="USD">US Dollar</option>
                        <option value="AFN">Afghan Afghani</option>
                        <option value="ALL">Albanian Lek</option>
                        <option value="DZD">Algerian Dinar</option>
                        <option value="AOA">Angolan Kwanza</option>
                        <option value="ARS">Argentine Peso</option>
                        <option value="AMD">Armenian Dram</option>
                        <option value="AWG">Aruban Florin</option>
                        <option value="AUD">Australian Dollar</option>
                        <option value="AZN">Azerbaijani Manat</option>
                        <option value="BSD">Bahamian Dollar</option>
                        <option value="BHD">Bahraini Dinar</option>
                        <option value="BDT">Bangladeshi Taka</option>
                        <option value="BBD">Barbadian Dollar</option>
                        <option value="BYR">Belarusian Ruble</option>
                        <option value="BEF">Belgian Franc</option>
                        <option value="BZD">Belize Dollar</option>
                        <option value="BMD">Bermudan Dollar</option>
                        <option value="BTN">Bhutanese Ngultrum</option>
                        <option value="BTC">Bitcoin</option>
                        <option value="BOB">Bolivian Boliviano</option>
                        <option value="BAM">
                            Bosnia-Herzegovina Convertible Mark
                        </option>
                        <option value="BWP">Botswanan Pula</option>
                        <option value="BRL">Brazilian Real</option>
                        <option value="GBP">British Pound Sterling</option>
                        <option value="BND">Brunei Dollar</option>
                        <option value="BGN">Bulgarian Lev</option>
                        <option value="BIF">Burundian Franc</option>
                        <option value="KHR">Cambodian Riel</option>
                        <option value="CAD">Canadian Dollar</option>
                        <option value="CVE">Cape Verdean Escudo</option>
                        <option value="KYD">Cayman Islands Dollar</option>
                        <option value="XOF">CFA Franc BCEAO</option>
                        <option value="XAF">CFA Franc BEAC</option>
                        <option value="XPF">CFP Franc</option>
                        <option value="CLP">Chilean Peso</option>
                        <option value="CNY">Chinese Yuan</option>
                        <option value="COP">Colombian Peso</option>
                        <option value="KMF">Comorian Franc</option>
                        <option value="CDF">Congolese Franc</option>
                        <option value="CRC">Costa Rican ColÃ³n</option>
                        <option value="HRK">Croatian Kuna</option>
                        <option value="CUC">Cuban Convertible Peso</option>
                        <option value="CZK">Czech Republic Koruna</option>
                        <option value="DKK">Danish Krone</option>
                        <option value="DJF">Djiboutian Franc</option>
                        <option value="DOP">Dominican Peso</option>
                        <option value="XCD">East Caribbean Dollar</option>
                        <option value="EGP">Egyptian Pound</option>
                        <option value="ERN">Eritrean Nakfa</option>
                        <option value="EEK">Estonian Kroon</option>
                        <option value="ETB">Ethiopian Birr</option>
                        <option value="EUR">Euro</option>
                        <option value="FKP">Falkland Islands Pound</option>
                        <option value="FJD">Fijian Dollar</option>
                        <option value="GMD">Gambian Dalasi</option>
                        <option value="GEL">Georgian Lari</option>
                        <option value="DEM">German Mark</option>
                        <option value="GHS">Ghanaian Cedi</option>
                        <option value="GIP">Gibraltar Pound</option>
                        <option value="GRD">Greek Drachma</option>
                        <option value="GTQ">Guatemalan Quetzal</option>
                        <option value="GNF">Guinean Franc</option>
                        <option value="GYD">Guyanaese Dollar</option>
                        <option value="HTG">Haitian Gourde</option>
                        <option value="HNL">Honduran Lempira</option>
                        <option value="HKD">Hong Kong Dollar</option>
                        <option value="HUF">Hungarian Forint</option>
                        <option value="ISK">Icelandic KrÃ³na</option>
                        <option value="INR">Indian Rupee</option>
                        <option value="IDR">Indonesian Rupiah</option>
                        <option value="IRR">Iranian Rial</option>
                        <option value="IQD">Iraqi Dinar</option>
                        <option value="ILS">Israeli New Sheqel</option>
                        <option value="ITL">Italian Lira</option>
                        <option value="JMD">Jamaican Dollar</option>
                        <option value="JPY">Japanese Yen</option>
                        <option value="JOD">Jordanian Dinar</option>
                        <option value="KZT">Kazakhstani Tenge</option>
                        <option value="KES">Kenyan Shilling</option>
                        <option value="KWD">Kuwaiti Dinar</option>
                        <option value="KGS">Kyrgystani Som</option>
                        <option value="LAK">Laotian Kip</option>
                        <option value="LVL">Latvian Lats</option>
                        <option value="LBP">Lebanese Pound</option>
                        <option value="LSL">Lesotho Loti</option>
                        <option value="LRD">Liberian Dollar</option>
                        <option value="LYD">Libyan Dinar</option>
                        <option value="LTL">Lithuanian Litas</option>
                        <option value="MOP">Macanese Pataca</option>
                        <option value="MKD">Macedonian Denar</option>
                        <option value="MGA">Malagasy Ariary</option>
                        <option value="MWK">Malawian Kwacha</option>
                        <option value="MYR">Malaysian Ringgit</option>
                        <option value="MVR">Maldivian Rufiyaa</option>
                        <option value="MRO">Mauritanian Ouguiya</option>
                        <option value="MUR">Mauritian Rupee</option>
                        <option value="MXN">Mexican Peso</option>
                        <option value="MDL">Moldovan Leu</option>
                        <option value="MNT">Mongolian Tugrik</option>
                        <option value="MAD">Moroccan Dirham</option>
                        <option value="MZM">Mozambican Metical</option>
                        <option value="MMK">Myanmar Kyat</option>
                        <option value="NAD">Namibian Dollar</option>
                        <option value="NPR">Nepalese Rupee</option>
                        <option value="ANG">
                            Netherlands Antillean Guilder
                        </option>
                        <option value="TWD">New Taiwan Dollar</option>
                        <option value="NZD">New Zealand Dollar</option>
                        <option value="NIO">Nicaraguan CÃ³rdoba</option>
                        <option value="NGN">Nigerian Naira</option>
                        <option value="KPW">North Korean Won</option>
                        <option value="NOK">Norwegian Krone</option>
                        <option value="OMR">Omani Rial</option>
                        <option value="PKR">Pakistani Rupee</option>
                        <option value="PAB">Panamanian Balboa</option>
                        <option value="PGK">Papua New Guinean Kina</option>
                        <option value="PYG">Paraguayan Guarani</option>
                        <option value="PEN">Peruvian Nuevo Sol</option>
                        <option value="PHP">Philippine Peso</option>
                        <option value="PLN">Polish Zloty</option>
                        <option value="QAR">Qatari Rial</option>
                        <option value="RON">Romanian Leu</option>
                        <option value="RUB">Russian Ruble</option>
                        <option value="RWF">Rwandan Franc</option>
                        <option value="SVC">Salvadoran ColÃ³n</option>
                        <option value="WST">Samoan Tala</option>
                        <option value="SAR">Saudi Riyal</option>
                        <option value="RSD">Serbian Dinar</option>
                        <option value="SCR">Seychellois Rupee</option>
                        <option value="SLL">Sierra Leonean Leone</option>
                        <option value="SGD">Singapore Dollar</option>
                        <option value="SKK">Slovak Koruna</option>
                        <option value="SBD">Solomon Islands Dollar</option>
                        <option value="SOS">Somali Shilling</option>
                        <option value="ZAR">South African Rand</option>
                        <option value="KRW">South Korean Won</option>
                        <option value="XDR">Special Drawing Rights</option>
                        <option value="LKR">Sri Lankan Rupee</option>
                        <option value="SHP">St. Helena Pound</option>
                        <option value="SDG">Sudanese Pound</option>
                        <option value="SRD">Surinamese Dollar</option>
                        <option value="SZL">Swazi Lilangeni</option>
                        <option value="SEK">Swedish Krona</option>
                        <option value="CHF">Swiss Franc</option>
                        <option value="SYP">Syrian Pound</option>
                        <option value="STD">São Tomé and Príncipe Dobra</option>
                        <option value="TJS">Tajikistani Somoni</option>
                        <option value="TZS">Tanzanian Shilling</option>
                        <option value="THB">Thai Baht</option>
                        <option value="TOP">Tongan pa'anga</option>
                        <option value="TTD">Trinidad & Tobago Dollar</option>
                        <option value="TND">Tunisian Dinar</option>
                        <option value="TRY">Turkish Lira</option>
                        <option value="TMT">Turkmenistani Manat</option>
                        <option value="UGX">Ugandan Shilling</option>
                        <option value="UAH">Ukrainian Hryvnia</option>
                        <option value="AED">United Arab Emirates Dirham</option>
                        <option value="UYU">Uruguayan Peso</option>
                        <option value="UZS">Uzbekistan Som</option>
                        <option value="VUV">Vanuatu Vatu</option>
                        <option value="VEF">Venezuelan BolÃ­var</option>
                        <option value="VND">Vietnamese Dong</option>
                        <option value="YER">Yemeni Rial</option>
                        <option value="ZMK">Zambian Kwacha</option>
                    </select>
                </div>
            </div>
            <div class="form-element">
                <label for="description">Description:</label>
                <textarea
                    placeholder="Enter a short description for your stash item"
                    v-model="description"
                />
            </div>

            <!-- FIBER AND YARN -->
            <div class="spacer" v-if="type == 'fiber' || type == 'yarn'" />
            <div class="form-element" v-if="type == 'fiber' || type == 'yarn'">
                <label for="dyerName">Dyer Name:</label>
                <input
                    type="text"
                    placeholder="Enter dyer information"
                    v-model="dyerName"
                />
            </div>
            <div class="form-element" v-if="type == 'fiber' || type == 'yarn'">
                <label for="colorwayName">Colorway Name:</label>
                <input
                    type="text"
                    placeholder="Enter colorway information"
                    v-model="colorwayName"
                />
            </div>
            <div class="form-element" v-if="type == 'fiber' || type == 'yarn'">
                <label for="fiberContent">Fiber Content:</label>
                <input
                    type="text"
                    placeholder="Enter fiber content information"
                    v-model="fiberContent"
                />
            </div>
            <!-- FIBER -->
            <div class="form-element" v-if="type == 'fiber'">
                <label for="fiberQuantity">Fiber Quantity:</label>
                <div class="input-select">
                    <input
                        type="text"
                        placeholder="Enter fiber quantity"
                        v-model="fiberQuantity"
                    />
                    <select v-model="fiberQuantityUnit">
                        <option value="null" selected disabled hidden>
                            unit
                        </option>
                        <option value="oz">oz</option>
                        <option value="g">grams</option>
                    </select>
                </div>
            </div>
            <!-- YARN -->
            <div class="form-element" v-if="type == 'yarn'">
                <label for="yarnWeight">Yarn Weight:</label>
                <select v-model="yarnWeight">
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
            <div class="form-element" v-if="type == 'yarn'">
                <label for="lengthPerSkein">Length / Skein:</label>
                <div class="input-select">
                    <input
                        type="text"
                        placeholder="Enter length per skein"
                        v-model="lengthPerSkein"
                    />
                    <select v-model="lengthUnit">
                        <option value="null" selected disabled hidden>
                            unit
                        </option>
                        <option value="yd">yards</option>
                        <option value="m">meters</option>
                    </select>
                </div>
            </div>
            <div class="form-element" v-if="type == 'yarn'">
                <label for="weightPerSkein">Weight / Skein:</label>
                <div class="input-select">
                    <input
                        type="text"
                        placeholder="Enter weight per skein"
                        v-model="weightPerSkein"
                    />
                    <select v-model="weightUnit">
                        <option value="null" selected disabled hidden>
                            unit
                        </option>
                        <option value="g">grams</option>
                        <option value="oz">oz</option>
                    </select>
                </div>
            </div>
            <div class="form-element" v-if="type == 'yarn'">
                <label for="amountStashed">Amount Stashed:</label>
                <div class="stashed-converter">
                    <div class="stashed-converter-inputs">
                        <input
                            type="text"
                            placeholder="0"
                            v-model="skeinsStashed"
                            id="skeinInput"
                            v-on:keyup="convert"
                        />
                        <p id="converter-text">Skeins</p>
                    </div>
                    <div class="stashed-converter-inputs">
                        <input
                            type="text"
                            placeholder="0"
                            v-model="lengthStashed"
                            id="lengthInput"
                            v-on:keyup="convert"
                        />
                        <p v-if="this.lengthUnit" id="converter-text">
                            {{ this.lengthUnit }}
                        </p>
                        <p v-else id="converter-text">—</p>
                    </div>
                    <div class="stashed-converter-inputs">
                        <input
                            type="text"
                            placeholder="0"
                            v-model="weightStashed"
                            id="weightInput"
                            v-on:keyup="convert"
                        />
                        <p v-if="this.weightUnit" id="converter-text">
                            {{ this.weightUnit }}
                        </p>
                        <p v-else id="converter-text">—</p>
                    </div>
                </div>
            </div>
            <div class="form-element" v-if="type == 'yarn'">
                <label for="handspun">Is Handspun?:</label>
                <button
                    id="handspun-button"
                    v-bind:class="{ selected: isHandspun }"
                    @click.prevent="toggleHandspun"
                >
                    Handspun
                </button>
            </div>
            <!-- COLOR SELECTOR -->
            <div class="spacer" v-if="type == 'fiber' || type == 'yarn'" />
            <div class="form-element" v-if="type == 'fiber' || type == 'yarn'">
                <label for="colors">Colors:</label>
                <div class="color-options">
                    <button
                        v-bind:class="{ selected: isRed }"
                        @click.prevent="this.isRed = !this.isRed"
                    >
                        Red
                    </button>
                    <button
                        v-bind:class="{ selected: isRedOrange }"
                        @click.prevent="this.isRedOrange = !this.isRedOrange"
                    >
                        Red-orange
                    </button>
                    <button
                        v-bind:class="{ selected: isOrange }"
                        @click.prevent="this.isOrange = !this.isOrange"
                    >
                        Orange
                    </button>
                    <button
                        v-bind:class="{ selected: isOrangeYellow }"
                        @click.prevent="
                            this.isOrangeYellow = !this.isOrangeYellow
                        "
                    >
                        Orange-yellow
                    </button>
                    <button
                        v-bind:class="{ selected: isYellow }"
                        @click.prevent="this.isYellow = !this.isYellow"
                    >
                        Yellow
                    </button>
                    <button
                        v-bind:class="{ selected: isYellowGreen }"
                        @click.prevent="
                            this.isYellowGreen = !this.isYellowGreen
                        "
                    >
                        Yellow-green
                    </button>
                    <button
                        v-bind:class="{ selected: isGreen }"
                        @click.prevent="this.isGreen = !this.isGreen"
                    >
                        Green
                    </button>
                    <button
                        v-bind:class="{ selected: isBlueGreen }"
                        @click.prevent="this.isBlueGreen = !this.isBlueGreen"
                    >
                        Blue-green
                    </button>
                    <button
                        v-bind:class="{ selected: isBlue }"
                        @click.prevent="this.isBlue = !this.isBlue"
                    >
                        Blue
                    </button>
                    <button
                        v-bind:class="{ selected: isBluePurple }"
                        @click.prevent="this.isBluePurple = !this.isBluePurple"
                    >
                        Blue-purple
                    </button>
                    <button
                        v-bind:class="{ selected: isPurple }"
                        @click.prevent="this.isPurple = !this.isPurple"
                    >
                        Purple
                    </button>
                    <button
                        v-bind:class="{ selected: isPink }"
                        @click.prevent="this.isPink = !this.isPink"
                    >
                        Pink
                    </button>
                    <button
                        v-bind:class="{ selected: isWhite }"
                        @click.prevent="this.isWhite = !this.isWhite"
                    >
                        White
                    </button>
                    <button
                        v-bind:class="{ selected: isGray }"
                        @click.prevent="this.isGray = !this.isGray"
                    >
                        Gray
                    </button>
                    <button
                        v-bind:class="{ selected: isBlack }"
                        @click.prevent="this.isBlack = !this.isBlack"
                    >
                        Black
                    </button>
                    <button
                        v-bind:class="{ selected: isCream }"
                        @click.prevent="this.isCream = !this.isCream"
                    >
                        Cream / Natural
                    </button>
                    <button
                        v-bind:class="{ selected: isBrown }"
                        @click.prevent="this.isBrown = !this.isBrown"
                    >
                        Brown
                    </button>
                    <button
                        v-bind:class="{ selected: isRainbow }"
                        @click.prevent="this.isRainbow = !this.isRainbow"
                    >
                        Rainbow
                    </button>
                </div>
            </div>
            <!-- NOTES -->
            <div class="spacer" />
            <div class="form-element">
                <label for="description">Notes:</label>
                <textarea
                    placeholder="Enter notes for your stash item"
                    v-model="notes"
                />
            </div>
            <div class="form-element">
                <div />
                <div class="option-buttons">
                    <button id="submit" type="submit">Edit</button>
                    <p class="option-button" id="cancel" @click="cancel">
                        Cancel
                    </p>
                    <p class="option-button" id="delete" @click="deleteStash">
                        Delete
                    </p>
                </div>
            </div>
        </form>
    </div>
</template>

<script>
export default {
    name: "StashEdit",
    mounted() {
        const data = loadStash(this.$route.params.stashId).then((data) => {
            if (data && data?.userId == this.$store.state.sessionUser?.id) {
                this.id = data.id;
                this.title = data.title;
                this.description = data.description;
                this.type = data.type;
                this.status = data.status;

                if (data.acquired) this.acquired = formatDate(data.acquired);

                this.acquiredFrom = data.acquiredFrom;
                this.acquiredPrice = data.acquiredPrice;
                this.acquiredCurrency = data.acquiredCurrency;

                this.dyerName = data.dyerName;
                this.colorwayName = data.colorwayName;

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
                    if (colorsArr.includes("rainbow")) this.isRainbow = true;
                }

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

                this.stashImages = data.stashItemImages;
            } else {
                this.$router.push("/404");
            }
        });
    },
    data() {
        return {
            validationErrors: [],
            id: null,
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

            notes: null,

            image: null,
            imageURL: "",
            imageStatus: "Upload",

            stashImages: [],
        };
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
                let colors = "";

                if (this.isRed) colors += "red ";
                if (this.isRedOrange) colors += "redorange ";
                if (this.isOrange) colors += "orange ";
                if (this.isOrangeYellow) colors += "orangeyellow ";
                if (this.isYellow) colors += "yellow ";
                if (this.isYellowGreen) colors += "yellowgreen ";
                if (this.isGreen) colors += "green ";
                if (this.isBlueGreen) colors += "bluegreen ";
                if (this.isBlue) colors += "blue ";
                if (this.isBluePurple) colors += "bluepurple ";
                if (this.isPurple) colors += "purple ";
                if (this.isPink) colors += "pink ";
                if (this.isWhite) colors += "white ";
                if (this.isGray) colors += "gray ";
                if (this.isBlack) colors += "black ";
                if (this.isCream) colors += "cream ";
                if (this.isBrown) colors += "brown ";
                if (this.isRainbow) colors += "rainbow ";

                const stashItem = {
                    id: this.id,
                    title: this.title,
                    description: this.description,
                    type: this.type,
                    status: this.status,

                    acquired: this.acquired,
                    acquired_from: this.acquiredFrom,
                    acquired_price: this.acquiredPrice,
                    acquired_currency: this.acquiredCurrency,

                    colors: colors,

                    dyer_name: this.dyerName,
                    colorway_name: this.colorwayName,

                    fiber_content: this.fiberContent,
                    fiber_quantity: this.fiberQuantity,
                    fiber_quantity_unit: this.fiberQuantityUnit,

                    yarn_weight: this.yarnWeight,
                    length_per_skein: this.lengthPerSkein,
                    length_unit: this.lengthUnit,
                    weight_per_skein: this.weightPerSkein,
                    weight_unit: this.weightUnit,
                    skeins_stashed: this.skeinsStashed,
                    length_stashed: this.lengthStashed,
                    weight_stashed: this.weightStashed,
                    is_handspun: this.isHandspun,

                    notes: this.notes,
                };
                const response = await fetch("/api/stash/", {
                    method: "PUT",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(stashItem),
                });
                if (response.ok) {
                    const data = await response.json();
                    this.$router.push(`/stash/${data.id}`);
                }
            }
        },
        cancel() {
            this.$router.back();
        },
        deleteStash() {
            this.$router.push(`/stash/${this.id}/delete`);
        },
        toggleHandspun: function () {
            this.isHandspun = !this.isHandspun;
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
                        stash_item_id: this.$route.params.stashId,
                        image_url: data.url,
                    };
                    const response = await fetch("/api/stash/images/", {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json",
                        },
                        body: JSON.stringify(image),
                    });
                    if (response.ok) {
                        const imageData = loadLinkedImages(
                            parseInt(this.$route.params.stashId)
                        ).then((imageData) => {
                            this.stashImages = imageData.linkedImages;
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

            const response = await fetch("/api/stash/images/", {
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
                    parseInt(this.$route.params.stashId)
                ).then((imageData) => {
                    this.stashImages = imageData.linkedImages;
                });
            }
        },
        convert($event) {
            if ($event.target.id == "skeinInput") {
                if (this.lengthPerSkein) {
                    this.lengthStashed =
                        this.skeinsStashed * this.lengthPerSkein;
                }
                if (this.weightPerSkein) {
                    this.weightStashed =
                        this.skeinsStashed * this.weightPerSkein;
                }
            } else if ($event.target.id == "lengthInput") {
                this.stashedLengthUnit = this.lengthUnit;
                if (this.lengthPerSkein) {
                    this.skeinsStashed =
                        this.lengthStashed / this.lengthPerSkein;
                }
                if (this.weightPerSkein) {
                    this.weightStashed =
                        (this.lengthStashed / this.lengthPerSkein) *
                        this.weightPerSkein;
                }
            } else if ($event.target.id == "weightInput") {
                this.stashedWeightUnit = this.weightUnit;
                if (this.weightPerSkein) {
                    this.skeinsStashed =
                        this.weightStashed / this.weightPerSkein;
                }
                if (this.lengthPerSkein) {
                    this.lengthStashed =
                        (this.weightStashed / this.weightPerSkein) *
                        this.lengthPerSkein;
                    this.stashedLengthUnit = this.lengthUnit;
                }
            }
        },
    },
};

const loadStash = async (id) => {
    const response = await fetch(`/api/stash/${id}`);
    if (response.ok) {
        const data = await response.json();
        return data;
    } else {
        const data = false;
        return data;
    }
};

const loadLinkedImages = async (id) => {
    const response = await fetch(`/api/stash/${id}/images`);
    if (response.ok) {
        const data = await response.json();
        return data;
    } else {
        const data = false;
        return data;
    }
};

const formatDate = (date) => {
    const d = new Date(date);
    let month = "" + (d.getMonth() + 1);
    let day = "" + d.getDate();
    let year = d.getFullYear();

    if (month.length < 2) {
        month = "0" + month;
    }
    if (day.length < 2) {
        day = "0" + day;
    }

    return [year, month, day].join("-");
};
</script>

<style scoped>
.stash-form-body {
    display: grid;
    grid-template-columns: 200px 1fr;
    column-gap: 100px;
    padding-left: 14%;
    padding-right: 14%;
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
    bottom: 6%;
    color: var(--color-nav);
    text-shadow: 0px 0px 10px var(--color-shadow);
    font-size: 20px;
}

.fa-trash-alt:hover {
    cursor: pointer;
}

.stash-image {
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

.stash-form {
    display: flex;
    flex-direction: column;
    font-family: "Open Sans", sans-serif;
}

.form-element {
    display: grid;
    grid-template-columns: 150px 1fr;
    column-gap: 16px;
    margin-bottom: 6px;
}

label {
    text-align: justify;
    font-size: 14px;
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
    font-size: 16px;
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
    font-size: 16px;
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

.image-input {
    width: 100%;
}

.image-input > input {
    width: 100%;
    border: none;
}

.stash-image {
    width: 100%;
    height: auto;
    object-fit: contain;
    border-radius: 6px;
    border: 1px solid var(--color-shadow);
}

#image-upload-button {
    width: 100%;
}

#file-upload-button {
    font-family: "Open Sans", sans-serif;
}

.input-select {
    display: grid;
    grid-template-columns: 1fr 120px;
    column-gap: 8px;
}

.input-select-input {
    margin-left: 20px;
    margin-right: -10px;
}

.spacer {
    height: 48px;
}

.stashed-converter {
    width: 100%;
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    column-gap: 8px;
}

.stashed-converter-inputs {
    width: 100%;
    display: grid;
    grid-template-columns: 55% calc(45% - 4px);
    column-gap: 2px;
}

.stashed-converter-inputs > input {
    width: auto;
    padding-right: 0px;
    min-width: 20px;
    font-size: 14px;
}

#converter-text {
    margin: 0px;
    align-self: center;
    font-size: 14px;
    margin-left: 4px;
    text-align: left;
}

#handspun-button {
    width: 100%;
}

.selected {
    background-color: var(--color-primary-contrast);
    color: white;
}
</style>
