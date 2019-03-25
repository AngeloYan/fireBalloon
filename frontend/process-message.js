const DialogFlow = require('dialogflow');

const projectId = 'fire-balloon-1552364979829';
const sessionId = '123456';
const languageCode = 'en';

const config = {
    credentials: {
        // private_key: process.env.DIALOGFLOW_PRIVATE_KEY,
        private_key: "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQClWnm/2aQWXZjv\nCITNf7bZkT+Y1iGEBBQag2kg8X+XSHDC/APk0El5rSIejOZXOVQmLdTOabzyuUfJ\n+Jv4ZWoXEAGTaa381MZpovAKqb11rkWq2l7d7cl9uKVwh6A/bTzQY44PD5ircNAS\nwQGTDcVWg2aeQTlQ+ez9bVvNMjG6eOPCrW7xok7B4m7V2zof8SxSHMkk92VIQoE/\n9Zr9ZoBDswlE1CSbquk1gu+qjjwYyNvA17923sskwGJ/tEp+bC4rN2IeoZFZ7/oc\nZJPpQY5yccOySUapWFNhmUTNaPD+IQSHX1cDvjOn7oqjXFFUtSIIsNEVkbG5o3Uv\nUvSOUL2jAgMBAAECggEAB5l05wBVrkF2+eVmVRt9h9pJFfkhaTPWyLEpb74powZN\nSGjUtPttpQ3z93t6Sp/z4h1RHnt1l6I0TnACmxPuIEk4CVJeELSmucwnRBYxAuuT\ngBqxKXn4PLLzx4w0LTYUCW/J459P4PE6XuJH9D45x5Qab0OIItSZs7wG8BNSfcNl\nkJhM9R4T3m9wiF3kQRmB2Tse/D75MlSYAYclpCyR2f8E79/W+rb55d4Msz308Nxg\nFGjdghvgoBLesSyFhbzi4434uoOkkU7QFztvx7U2+gBRztcU+cYVt08IZtu5V2Bw\nNXucV3Ud4hI2tacd+C0WjaoZxRLlcssiy3OPDzjrwQKBgQDkW0RyqMYlo78LPyzt\nYn0RZEFgJuheCRc/U6l42hudfWJCaNE+sZKZ2RF9DAAeCnBXnj1yNJlU9DFclqsg\nzVvTbb/aXWtxJKjOXioRaDQYywRwOS4u0mSy3F2ZKIzBqu6Xi4maSWyzR0ARLhdF\nHUtfJnPSz0SYDRDdXLoOfc2x2QKBgQC5XsCREovX0gr/pyItjFj/KJcOnP/yZcYW\nOeIh2we9KNV1BRUDnW9Kh5/OTWpnlz5CHRU1jESModAQGxQnHqurRr44f+erhDRa\nfFBaHrc32HFsBcd5reUNMYk1gzEpSCqkPHH4TWclVXRFyyCz4ijvL7JVCbqyhL7+\nnVyCjk3B2wKBgFOg/QtEtfRY6IE07L4vAICbB7ov5Y9yotnlSL5imhRuM8sAWgks\nvPSs41O5Tl2yEvxzjitCChlrqJww7ZEAxC1FFyrgZZW1CEEziRKA5/tgdkqnFju9\nf3VlcL3DdPEEKYbEamtfkniBknv4NjtwhAbfrTE6CPPqbQ+0gssF1YvZAoGBAKY3\nNTqgQ67RE7WrmvT2rPKW5eRfmQ00fwt8+azb5rOSAt08IlysdZeBxyTIvAmJT3Ue\n+N6cGPd1PMjETyzIzqv08ipdXlGoaP1eDPrSIf28Ye+3uub7q7BJ47uNGK7om/vK\ni3NXjI6ocmsGuhsyRvw6a5De+X6Lk2thlQsoKMcTAoGBAJfGHTCa5drJItFZwqSq\nDkIYIolUC5xHW3K+PcX/r8jg9NljFP5rPGb6l6MgB/TpTkmkIHTCpHAHAspuqCjt\nuUvYubxkvlxIKfy5P+x27OKrqaXoP13vbpI7Cv5zPLodi9I5YfsdWaD8B5M91+uH\nk267m3I03zZQN75vp8XBK7Az\n-----END PRIVATE KEY-----\n",
        // client_email: process.env.DIALOGFLOW_CLIENT_EMAIL,
        client_email: "dialogflow-aeaxio@fire-balloon-1552364979829.iam.gserviceaccount.com",
    },
};

const sessionClient = new DialogFlow.SessionsClient(config);

const sessionPath = sessionClient.sessionPath(projectId, sessionId);

const processMessage = message => {
    const request = {
        session: sessionPath,
        queryInput: {
            text: {
                text: message,
                languageCode,
            },
        },
    };

    sessionClient
        .detectIntent(request)
        .then(responses => {
            console.log(responses);
            const result = responses[0].queryResult;
            console.log(result.fulfillmentText);
            return result.fulfillmentText;
        })
        .catch(err => {
            console.error('ERROR:', err);
        });
};

module.exports = processMessage;