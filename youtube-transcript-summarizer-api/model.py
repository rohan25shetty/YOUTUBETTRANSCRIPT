import re
import nltk
import spacy
from string import punctuation
from transcript import get_transcript_of_yt_video
from translate import g_translate
from download import makeTextFile

nltk.download('stopwords')


def text_summarizer(text):

    from heapq import nlargest
    from nltk.corpus import stopwords

    nlp = spacy.load('en_core_web_sm')
    stop_words = stopwords.words('english')

    doc = nlp(text)
    # tokens=[token.text for token in doc]

    word_frequencies = {}
    for word in doc:
        if word.text.lower() not in stop_words:
            if word.text.lower() not in punctuation:
                if word.text not in word_frequencies.keys():
                    word_frequencies[word.text] = 1
                else:
                    word_frequencies[word.text] += 1

    max_frequency = max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word] = word_frequencies[word]/max_frequency

    sentence_tokens = [sent for sent in doc.sents]

    sentence_scores = {}
    for sent in sentence_tokens:
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word.text.lower()]
                else:
                    sentence_scores[sent] += word_frequencies[word.text.lower()]

    select_length = int(len(sentence_tokens)*0.3)
    summary = nlargest(select_length, sentence_scores, key=sentence_scores.get)

    summary = [re.sub('[.]', '', (word.text).replace(
        "\n", ",").strip()).capitalize() for word in summary]
    final_text = '. '.join(summary)

    final_summary = re.sub(',,|,\.|,\-|[\"]', '', final_text)

    return final_summary


def nlp_model(v_id):

    transcript = get_transcript_of_yt_video(v_id)

    if (transcript == '0'):
        return '0'

    else:
        transcript_size = len(transcript)

        original_text = ' '.join([t['text'] for t in transcript])
        original_text_length = len(original_text)

        s_t = []

        result = ""

        for txt in range(0, transcript_size):
            if (txt != 0 and txt % 100 == 0):
                result += ' ' + transcript[txt]['text']
                s_t.append(text_summarizer(result))
                result = ""
            else:
                result += ' ' + transcript[txt]['text']

            if (txt == transcript_size - 1):
                result += ' ' + transcript[txt]['text']
                s_t.append(text_summarizer(result))

        english_summary = ' '.join(s_t) + '.'

        final_summary_length = len(english_summary)

        hindi_translated_summary = g_translate(english_summary, 'hi')

        kannada_translated_summary = g_translate(english_summary, 'kn')

        # print(original_text_length, '-->', final_summary_length)
        # print(final_smy)

        makeTextFile("English", english_summary)
        makeTextFile("Hindi", hindi_translated_summary)
        makeTextFile("Kannada", kannada_translated_summary)

        return original_text_length, final_summary_length, english_summary, hindi_translated_summary, kannada_translated_summary
