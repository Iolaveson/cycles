from game.scripting.action import Action


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        score1= cast.get_first_actor("scores1")
        score2= cast.get_first_actor("scores2")

        food = cast.get_first_actor("foods")
        snake1 = cast.get_first_actor("snake1")
        snake2 = cast.get_first_actor("snake2")
        messages = cast.get_actors("messages")
        snake1_segments = snake1.get_segments()
        snake2_segments = snake2.get_segments()

        self._video_service.clear_buffer()
        self._video_service.draw_actor(food)
        self._video_service.draw_actors(snake1_segments)
        self._video_service.draw_actors(snake2_segments)
        self._video_service.draw_actor(score1)
        self._video_service.draw_actor(score2)
        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()